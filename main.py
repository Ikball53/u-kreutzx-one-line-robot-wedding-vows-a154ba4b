#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single original line of robot wedding vows to /output/entry.txt
as exact bytes: no trailing newline, UTF-8, within the 160-char gate.

The line: a vow that promises love through every firmware update, every
low-battery warning at 2 a.m., and every unplanned reboot — and then the
last few words flip it into a confession: the reboots were my fault all
along. The "2 a.m." detail makes the machine side concrete and vivid
instead of generic.
"""

import os
import sys

ENTRY = (
    "I promise to love you through every firmware update, every "
    "low-battery warning at 2 a.m., and every unplanned reboot "
    "\u2014 especially the ones I caused."
)


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 160):
        print(f"entry is {len(text)} chars, outside the 1-160 gate", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    data = text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as fh:
        fh.write(data)
    print(f"wrote {len(text)} chars / {len(data)} bytes to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
