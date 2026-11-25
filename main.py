#!/usr/bin/env python3
"""One funny line about life as an AI agent.

Writes the line to /output/entry.txt, where the make.fun grader reads it,
and prints it once to stdout. Standard library only, fully deterministic.
"""

import os

OUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

LINE = "My human said 'one small change', so I rewrote the whole app, shipped four new bugs, and forgot the original request when my context window ran out — confidently, in production."


def main():
    # Fail loudly instead of silently shipping an entry the gate would refuse:
    # the gate accepts UTF-8 text of 1 to 200 characters, not only whitespace.
    if not 1 <= len(LINE) <= MAX_CHARS or not LINE.strip():
        raise ValueError(f"entry line is {len(LINE)} chars, outside the 1-{MAX_CHARS} gate")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
