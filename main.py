"""Entry program for 'Make the AI Judge Feel Proud: A Family Scene'.

The whole entry is a short family scene, under 280 characters: Dad
still calls every Sunday to ask if I have eaten, then stays on the
line while I cook, narrating each step like a sports commentator.
He says it is quality time. It is. The warmth is the weekly ritual;
the joke is the play-by-play commentary; the heart is the last line
agreeing with him. The program asserts the 280-character cap
before writing, so the gate can never fail on length.
"""

import sys
from pathlib import Path

LINE = "Dad still calls every Sunday to ask if I've eaten, then stays on the line while I cook, narrating each step like a sports commentator. He says it's quality time. It is."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} characters, over the 280 limit"
    assert LINE.count("\n") <= 1, "entry must be at most two lines"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
