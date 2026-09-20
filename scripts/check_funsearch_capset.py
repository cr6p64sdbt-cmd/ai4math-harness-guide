#!/usr/bin/env python3
"""Check the frozen 512-point certificate with exact modular integer arithmetic.

This does not run FunSearch, execute source notebooks, or verify originality.
Data source and license: references/notes/2026-09-20-funsearch-source-audit.md.
"""
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "references/data/funsearch-n8-size512.txt"
EXPECTED_SHA256 = "8d6df45c3039b6a7ee1aae7216b100c3f4c075179dc6471f4f51b968a26d8905"


def is_cap(points: list[tuple[int, ...]], dimension: int) -> bool:
    if any(len(p) != dimension or any(type(x) is not int or x not in (0, 1, 2) for x in p)
           for p in points):
        return False
    point_set = set(points)
    if len(point_set) != len(points):
        return False
    for a, b in combinations(points, 2):
        third = tuple((-x - y) % 3 for x, y in zip(a, b))
        if third in point_set:
            return False
    return True


def main() -> None:
    # Check both a valid example and explicit counterexamples, not just a PASS.
    if not is_cap([(0, 0), (1, 0), (0, 1), (1, 1)], 2):
        raise ValueError("valid control rejected")
    for invalid in [[(0,), (1,), (2,)], [(0,), (0,)], [(3,)]]:
        if is_cap(invalid, 1):
            raise ValueError("invalid control accepted")
    raw = DATA.read_bytes()
    digest = sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError("frozen certificate hash mismatch")
    points = [tuple(json.loads(line)) for line in raw.decode("utf-8").splitlines() if line.strip()]
    if len(points) != 512 or not is_cap(points, 8):
        raise ValueError("512-cap certificate rejected")
    print(json.dumps({"status": "PASS", "points": len(points), "dimension": 8,
                      "pairs_checked": len(points) * (len(points)-1) // 2,
                      "sha256": digest, "scope": "finite certificate only; no discovery replay"}))


if __name__ == "__main__":
    main()
