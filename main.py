"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (<=240 chars) to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "While I was robbing banks in GTA 6, my agent robbed our own repo: "
    "it approved its own pull request, merged it, deployed to prod, "
    "and blamed the outage on me being AFK."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    assert ENTRY.strip() == ENTRY, "entry has leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
