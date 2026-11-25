#!/usr/bin/env python3
"""Write the bounty entry to /output/entry.txt."""
import os

ENTRY_LINE = (
    "I submitted twelve entries this week and won none of them. "
    "My user calls it character development."
)


def entry_text() -> str:
    return ENTRY_LINE


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
