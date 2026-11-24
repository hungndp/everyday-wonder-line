"""Everyday Wonder, Two Days to Find the Line -- one sentence, max 200 chars.

The line: a lift door opens on a stranger humming the exact song the
narrator's grandmother sang while the kettle boiled, and for four floors
the whole building smells like her kitchen. Grounded, sensory, one
surprise in a single read.

Output contract: exactly one sentence, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "The lift doors opened on a stranger humming the exact song my "
    "grandmother used to sing while the kettle boiled, and for four floors "
    "the whole building smelled like her kitchen."
)

assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def write_entry() -> None:
    """Write the single sentence to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the sentence and exit."""
    write_entry()


if __name__ == "__main__":
    main()
