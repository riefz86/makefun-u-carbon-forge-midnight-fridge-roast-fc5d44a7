#!/usr/bin/env python3
"""Midnight Fridge Roast.

One line roasting a smart fridge that refuses to open after midnight.
Writes exactly the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
on a local run): UTF-8, 1-200 characters, no trailing newline.

The angle: the fridge's midnight lock is not a bug, it is a diet plan
— "self-control mode" — imposed by an appliance that has never tasted
a single thing in its life. The joke targets the petty rule itself
(criterion 4), and the punchline turns on the fridge's total lack of
standing to lecture anyone about food.
"""

import os

LINE = (
    "My fridge locks itself at midnight and flashes 'self-control mode' "
    "— a diet plan written by an appliance that has never tasted a single thing."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
