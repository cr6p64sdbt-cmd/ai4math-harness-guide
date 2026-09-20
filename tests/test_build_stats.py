from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_stats.py"
SPEC = importlib.util.spec_from_file_location("build_stats", SCRIPT)
assert SPEC and SPEC.loader
build_stats = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build_stats)


def card_text(
    *,
    event_id: str,
    status: str,
    evidence: str,
    reading: str,
    sources: str,
    event_type: str = "preprint",
) -> str:
    return f'''---
id: "{event_id}"
title: "Fixture {event_id}"
event_date: "2026-08-20"
retrieved_at: "2026-08-24"
area: ["test-area"]
event_type: "{event_type}"
source_claim: "A bounded test claim"
mathematical_status: "{status}"
evidence_level: "{evidence}"
source_reading_status: "{reading}"
ai_roles: ["proof-search"]
human_roles: ["problem-selection"]
autonomy_evidence: "UNKNOWN"
primary_sources: {sources}
system_records: []
score_math_importance: 3
score_ai_centrality: 2
score_source_strength: 1
score_mechanism_auditability: 1
signal_score: 7
dossier: null
---

# Fixture
'''


class BuildStatsTests(unittest.TestCase):
    def write_card(self, root: Path, name: str, content: str) -> Path:
        path = root / "events" / "2026" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_locator_only_remains_unassessed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_card(
                root,
                "locator.md",
                card_text(
                    event_id="locator",
                    status="UNASSESSED",
                    evidence="LOCATOR-ONLY",
                    reading="locator-only",
                    sources="[]",
                    event_type="news-locator",
                ),
            )
            cards = build_stats.load_cards(root)
            self.assertEqual(cards[0][1]["mathematical_status"], "UNASSESSED")

    def test_primary_preprint_can_remain_open(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_card(
                root,
                "preprint.md",
                card_text(
                    event_id="preprint",
                    status="OPEN",
                    evidence="PRIMARY-SOURCE-CHECKED",
                    reading="section-summary",
                    sources='["https://arxiv.org/abs/example"]',
                ),
            )
            cards = build_stats.load_cards(root)
            self.assertEqual(cards[0][1]["evidence_level"], "PRIMARY-SOURCE-CHECKED")

    def test_correction_does_not_force_status_promotion(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_card(
                root,
                "correction.md",
                card_text(
                    event_id="correction",
                    status="OPEN",
                    evidence="PRIMARY-SOURCE-CHECKED",
                    reading="section-summary",
                    sources='["https://example.org/primary-correction"]',
                    event_type="correction",
                ),
            )
            cards = build_stats.load_cards(root)
            self.assertEqual(cards[0][1]["mathematical_status"], "OPEN")

    def test_primary_source_alone_cannot_mark_disproved(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_card(
                root,
                "overclaim.md",
                card_text(
                    event_id="overclaim",
                    status="DISPROVED",
                    evidence="PRIMARY-SOURCE-CHECKED",
                    reading="section-summary",
                    sources='["https://arxiv.org/abs/example"]',
                ),
            )
            with self.assertRaises(build_stats.CardError):
                build_stats.load_cards(root)

    def test_stats_render_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_card(
                root,
                "one.md",
                card_text(
                    event_id="one",
                    status="OPEN",
                    evidence="PRIMARY-SOURCE-CHECKED",
                    reading="section-summary",
                    sources='["https://arxiv.org/abs/example"]',
                ),
            )
            cards = build_stats.load_cards(root)
            self.assertEqual(build_stats.render_stats(root, cards), build_stats.render_stats(root, cards))


if __name__ == "__main__":
    unittest.main()
