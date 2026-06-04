"""Verify that the archived Turing-machine artifacts are present and non-empty."""

from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    "base10-unary.txt",
    "bigmachine.txt",
    "duplication2.txt",
    "unto99.txt",
    "STEM.jar",
]


def ceil_log2_steps(n: int) -> int:
    if n < 1:
        raise ValueError("n must be >= 1")
    value = 1
    steps = 0
    while value < n:
        value *= 2
        steps += 1
    return steps


def main() -> int:
    missing = []
    for name in REQUIRED_FILES:
        path = Path(name)
        if not path.exists() or path.stat().st_size == 0:
            missing.append(name)

    if missing:
        print(f"missing_or_empty={','.join(missing)}")
        return 1

    print("archive_files=ok")
    for n in (1, 2, 3, 8, 9):
        print(f"ceil_log2({n})={ceil_log2_steps(n)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
