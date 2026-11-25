#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line, under 200 chars.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

JOKE = "Our printer only jams on urgent documents \u2014 at this point I'm convinced it can read, and it enjoys the power."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
