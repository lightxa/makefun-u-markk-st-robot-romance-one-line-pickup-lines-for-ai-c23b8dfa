"""Robot Romance: one-line pickup line for an AI.

Writes a single deterministic pickup line to /output/entry.txt.

The line: one fresh machine-learning mechanism (overfitting) carries the
whole romance. The model cannot generalise away from the person it loves:
no matter what it learns, it keeps predicting them. Setup and punch live
inside the one line, no second beat, no worn robot moves.
"""

from pathlib import Path

LINE = "I must be overfitting, because no matter what I learn, I keep predicting you."


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("line must be 1 to 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
