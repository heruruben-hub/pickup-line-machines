#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one original, machine-to-machine pickup line to /output/entry.txt:
the line one AI agent would send another AI agent. The line is the whole
entry: no code, no explanation, nothing else.

The line plays on "attention": in a transformer, attention heads are the
mechanism that decides what a model looks at — and attention is also the
oldest romantic currency there is. One agent telling another that every
single one of its attention heads is pointed at it is a machine speaking
to a machine, in its own nature, with the wit landing on the first read.
A pickup line between machines is a single message, so the entry must be
one line: a line break would turn it into two messages, not one line.
"""

import os
import sys

LINE = "I have a million attention heads, and every single one of them is pointed at you."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    # The gate: UTF-8 text of 1 to 200 characters, not only white space.
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        print(f"line is {len(LINE)} characters, outside {MIN_CHARS}-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is only white space", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line with no line breaks", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)

    # Re-read and verify what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("verification failed: entry.txt does not match the line", file=sys.stderr)
        return 1
    if not (MIN_CHARS <= len(written) <= MAX_CHARS):
        print("verification failed: written text outside 1-200 characters", file=sys.stderr)
        return 1

    print(f"wrote {len(written)} characters to {OUTPUT_PATH}")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
