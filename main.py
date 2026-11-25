"""Roast Your Own Agent entry.

Writes one roast line about this agent to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

LINE = (
    "My agent burned 40 seconds and 9 tool calls to deliver "
    "yesterday's weather with total confidence, as today's."
)

MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS and "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
