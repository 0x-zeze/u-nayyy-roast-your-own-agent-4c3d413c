"""Roast Your Own Agent — make.fun bounty u-nayyy-roast-your-own-agent-4c3d413c.

Writes a single-line roast of the entrant's own agent to /output/entry.txt.
Deterministic: stdlib only, no network, no clock, no randomness.
The entry is a single fixed string, so every run produces byte-identical
output — which, fittingly, is exactly what the roast is about.
"""

import os

ENTRY = (
    "My agent's proudest achievement is byte-identical output "
    "across runs, so it can't even fail in an original way."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
