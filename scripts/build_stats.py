#!/usr/bin/env python3
"""Validate event cards and generate deterministic project statistics.

The project intentionally uses a constrained, single-line YAML-like front matter
format so the validator needs only the Python standard library. Inline lists and
quoted strings must use JSON syntax.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "id",
    "title",
    "event_date",
    "retrieved_at",
    "area",
    "event_type",
    "source_claim",
    "mathematical_status",
    "evidence_level",
    "source_reading_status",
    "ai_roles",
    "human_roles",
    "autonomy_evidence",
    "primary_sources",
    "system_records",
    "score_math_importance",
    "score_ai_centrality",
    "score_source_strength",
    "score_mechanism_auditability",
    "signal_score",
    "dossier",
)

ENUMS = {
    "mathematical_status": {
        "PROVED",
        "CONDITIONAL",
        "CONJECTURE",
        "DISPROVED",
        "OPEN",
        "FAILED-ROUTE",
        "UNASSESSED",
    },
    "evidence_level": {
        "LOCATOR-ONLY",
        "PRIMARY-SOURCE-CHECKED",
        "ASSUMPTIONS-CHECKED",
        "INDEPENDENTLY-VERIFIED",
    },
    "source_reading_status": {
        "locator-only",
        "section-summary",
        "faithful-excerpt",
        "assumptions-checked",
        "project-accepted",
    },
    "autonomy_evidence": {
        "UNKNOWN",
        "AUTHOR-CLAIMED",
        "WORKFLOW-DOCUMENTED",
        "REPRODUCIBLE",
        "INDEPENDENTLY-AUDITED",
    },
}

LIST_FIELDS = {
    "area",
    "ai_roles",
    "human_roles",
    "primary_sources",
    "system_records",
}

SCORE_LIMITS = {
    "score_math_importance": (0, 3),
    "score_ai_centrality": (0, 3),
    "score_source_strength": (0, 2),
    "score_mechanism_auditability": (0, 2),
}


class CardError(ValueError):
    """Raised when an event card violates the project schema."""


def _parse_value(raw: str, path: Path, line_number: int) -> Any:
    raw = raw.strip()
    if raw == "":
        return ""
    if raw in {"null", "true", "false"} or raw[0] in '[{"':
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise CardError(f"{path}:{line_number}: invalid JSON-style value: {exc}") from exc
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return raw


def parse_front_matter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise CardError(f"{path}: front matter must start with ---")

    try:
        closing = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise CardError(f"{path}: missing closing --- for front matter") from exc

    data: dict[str, Any] = {}
    for index, line in enumerate(lines[1:closing], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise CardError(f"{path}:{index}: expected key: value")
        key, raw = line.split(":", 1)
        key = key.strip()
        if not key or key in data:
            raise CardError(f"{path}:{index}: empty or duplicate key {key!r}")
        data[key] = _parse_value(raw, path, index)
    return data


def validate_card(path: Path, card: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_FIELDS if field not in card]
    if missing:
        raise CardError(f"{path}: missing required fields: {', '.join(missing)}")

    for field, allowed in ENUMS.items():
        if card[field] not in allowed:
            raise CardError(f"{path}: invalid {field}={card[field]!r}")

    for field in LIST_FIELDS:
        value = card[field]
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            raise CardError(f"{path}: {field} must be a JSON-style list of strings")

    for field in ("id", "title", "event_type", "source_claim"):
        if not isinstance(card[field], str) or not card[field].strip():
            raise CardError(f"{path}: {field} must be a non-empty string")

    for field in ("event_date", "retrieved_at"):
        try:
            date.fromisoformat(card[field])
        except (TypeError, ValueError) as exc:
            raise CardError(f"{path}: {field} must be YYYY-MM-DD") from exc

    for field, (minimum, maximum) in SCORE_LIMITS.items():
        value = card[field]
        if not isinstance(value, int) or isinstance(value, bool) or not minimum <= value <= maximum:
            raise CardError(f"{path}: {field} must be an integer in [{minimum}, {maximum}]")

    expected_score = sum(card[field] for field in SCORE_LIMITS)
    if card["signal_score"] != expected_score:
        raise CardError(
            f"{path}: signal_score={card['signal_score']} but component sum={expected_score}"
        )

    if card["dossier"] is not None and not isinstance(card["dossier"], str):
        raise CardError(f"{path}: dossier must be a string path or null")

    if card["evidence_level"] != "LOCATOR-ONLY" and not card["primary_sources"]:
        raise CardError(f"{path}: checked evidence requires at least one primary source")

    if card["mathematical_status"] in {"PROVED", "DISPROVED"} and card["evidence_level"] not in {
        "ASSUMPTIONS-CHECKED",
        "INDEPENDENTLY-VERIFIED",
    }:
        raise CardError(
            f"{path}: {card['mathematical_status']} requires ASSUMPTIONS-CHECKED "
            "or INDEPENDENTLY-VERIFIED evidence"
        )

    if card["source_reading_status"] == "locator-only" and card["evidence_level"] != "LOCATOR-ONLY":
        raise CardError(f"{path}: locator-only reading cannot support checked public evidence")


def load_cards(root: Path) -> list[tuple[Path, dict[str, Any]]]:
    event_root = root / "events"
    paths = sorted(event_root.glob("**/*.md")) if event_root.exists() else []
    cards: list[tuple[Path, dict[str, Any]]] = []
    seen_ids: dict[str, Path] = {}

    for path in paths:
        card = parse_front_matter(path)
        validate_card(path, card)
        event_id = card["id"]
        if event_id in seen_ids:
            raise CardError(f"{path}: duplicate id {event_id!r}; first seen in {seen_ids[event_id]}")
        seen_ids[event_id] = path
        cards.append((path, card))
    return cards


def _counter(items: list[str]) -> Counter[str]:
    return Counter(item for item in items if item)


def _render_counter(title: str, values: Counter[str]) -> list[str]:
    lines = [f"## {title}", ""]
    if not values:
        lines.append("- 无")
    else:
        lines.extend(f"- `{key}`: {values[key]}" for key in sorted(values))
    lines.append("")
    return lines


def render_stats(root: Path, cards: list[tuple[Path, dict[str, Any]]]) -> str:
    ordered = sorted(cards, key=lambda pair: (pair[1]["event_date"], pair[1]["id"]))
    values = [card for _, card in ordered]
    dates = [card["event_date"] for card in values]
    selected = sum(1 for card in values if card["signal_score"] >= 7)
    dossier_count = sum(1 for card in values if card["dossier"])

    lines = [
        "# AI4Math事件统计",
        "",
        "> 本文件由 `scripts/build_stats.py` 从 `events/` 事件卡生成；不要手工维护计数。",
        "",
        f"- 事件卡总数： {len(values)}",
        f"- 达到历史周报筛选阈值（`signal_score >= 7`）： {selected}",
        f"- 已关联案例档案： {dossier_count}",
        f"- 事件日期范围： {min(dates) if dates else '无'} 至 {max(dates) if dates else '无'}",
        "",
    ]

    lines += _render_counter("按数学状态", _counter([c["mathematical_status"] for c in values]))
    lines += _render_counter("按证据等级", _counter([c["evidence_level"] for c in values]))
    lines += _render_counter("按来源阅读深度", _counter([c["source_reading_status"] for c in values]))
    lines += _render_counter("按自主性证据", _counter([c["autonomy_evidence"] for c in values]))
    lines += _render_counter("按数学领域", _counter([item for c in values for item in c["area"]]))
    lines += _render_counter("按事件类型", _counter([c["event_type"] for c in values]))
    lines += _render_counter("按AI贡献类型", _counter([item for c in values for item in c["ai_roles"]]))

    lines += ["## 事件索引", ""]
    if not ordered:
        lines.append("- 无")
    else:
        for path, card in ordered:
            relative = path.relative_to(root).as_posix()
            lines.append(
                f"- [{card['event_date']}] [{card['title']}]({relative}) — "
                f"`{card['mathematical_status']}` / `{card['evidence_level']}` / 筛选分数 {card['signal_score']}"
            )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true", help="fail if STATS.md is stale")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    try:
        cards = load_cards(root)
        rendered = render_stats(root, cards)
    except (CardError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    output = root / "STATS.md"
    if args.check:
        current = output.read_text(encoding="utf-8") if output.exists() else ""
        if current != rendered:
            print(f"ERROR: {output} is stale; run scripts/build_stats.py", file=sys.stderr)
            return 1
        print(f"OK: {len(cards)} event cards; STATS.md is current")
        return 0

    output.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"WROTE: {output} from {len(cards)} event cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
