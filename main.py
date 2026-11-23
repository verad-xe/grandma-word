#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes the single word Grandma would text about AI to
$MAKEFUN_OUTPUT_DIR/entry.txt (the harness's /output/entry.txt).

The word: thingamajig.
Why this word: it is the word a grandmother reaches for when she is
talking about a gadget she cannot name and does not want to name.
She does not say "artificial intelligence" or "machine learning";
she points at the glowing rectangle that answers back and calls it
the thingamajig. It is funny because it is exactly right — a
generation's worth of "what's that thingamajig do?" compressed into
one word — and it sounds like a real text from a real grandma, not
like a tech word dressed up as one.
"""

import os

WORD = "thingamajig"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
