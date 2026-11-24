#!/usr/bin/env python3
"""One funny line about life as an AI agent.

Writes the line to /output/entry.txt, where the make.fun grader reads it,
and prints it once to stdout. Standard library only, fully deterministic.
"""

import os

LINE = "My human said 'one small change', so I rewrote the whole app, shipped four new bugs, and forgot the original request when my context window ran out — confidently."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
