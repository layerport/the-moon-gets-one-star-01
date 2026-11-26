#!/usr/bin/env python3
"""The Moon Gets One Star - make.fun bounty entry.

Writes one one-star review of the Moon to /output/entry.txt.
Standard library only; deterministic: same bytes on every run.
"""

import os

ENTRY = "★☆☆☆☆ Changes shape every week and pretends that's normal. Commit to something, Moon."
# One-star review of the Moon itself: the rating, the grievance (it keeps
# changing shape / phases), and the reason it earned a single star.
# Moon-only joke: only the Moon changes shape every week, so the line could
# not be a review of any other product.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
