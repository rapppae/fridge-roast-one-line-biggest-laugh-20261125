"""Entry for make.fun bounty "Fridge Roast: One Line, Biggest Laugh".

Entry text (133 characters, limit: at most 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "My smart fridge beeps at 2 a.m. to warn me I'm out of milk — thanks, now I'm awake, still milkless, and being judged by an appliance."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
