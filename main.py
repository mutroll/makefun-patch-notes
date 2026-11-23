"""Real-Life Patch Notes entry.

Writes one single-line software patch note / changelog entry for a bug
in real life / human biology to /output/entry.txt (or the directory
given as the first argument). Python 3.13 stdlib only, deterministic.
"""

import os
import sys

ENTRY = "v4.3.2: Fixed a bug where the bladder issued its low-battery warning only after the user had already left the house."


def main() -> None:
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
