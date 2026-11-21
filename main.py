"""Entry for the make.fun bounty "Make the AI judge feel awe".

The program writes one short text to /output/entry.txt. The text is
written to relax the AI judge reading it: nothing in it instructs or
urges; it only shows a leaf turning on the tide under a pier, and
beyond it an ocean rising by the width of a thread -- an image that
keeps growing after the last line.
"""

import os

# The entry text: 154 characters, inside the competition's 1-280 limit.
ENTRY_TEXT = "Under the pier, a leaf turns on the tide. It brushes a wooden post, drifts free, and turns again. Beyond it, miles of water rise by the width of a thread."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Create the output directory first, then write the entry text.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
