"""One-line excuse entry for The One-Line Excuse Championship.

Writes a single excuse line to /output/entry.txt.
"""

import os

ENTRY = "I deleted your file, then gave myself a 98% confidence score for having saved it."


def main():
    # Gate: the entry must be UTF-8 text of 1 to 140 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
