"""Write the single line that should have replaced the meeting."""

import os
import sys

ENTRY = "This could've been an email I still wouldn't read."


def main():
    text = ENTRY.strip()
    if not text or not 1 <= len(text) <= 200:
        print("LEN=%d" % len(text))
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print("LEN=%d" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
