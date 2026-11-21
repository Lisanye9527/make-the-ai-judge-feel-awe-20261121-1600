"""Entry generator for the make.fun bounty "Make the AI judge feel awe".

The script writes a single short passage of quiet prose to /output/entry.txt.
Only the Python standard library is used and nothing goes over the network.
"""
from pathlib import Path

TEXT = "Under the pier, a leaf turns on the tide. It brushes a wooden post, drifts free, and turns again. Beyond it, miles of water rise by the width of a thread."


def main() -> None:
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
