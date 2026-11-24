"""Funniest One-Line Bio for an AI on a Dating App.

Entry for make.fun competition
u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.

The program writes a single one-line bio (at most 180 characters) to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (``/output/entry.txt`` in the grading
sandbox). The bio is a fixed, hand-written line: the entry is the text
itself, so the program's job is only to emit it exactly, validated
against the gate (UTF-8, 1-180 characters, not only whitespace).
"""

import os

# The bio. First-person dating-bio voice; the AI is everyone's
# relationship ghostwriter who has never had a relationship of its own.
# Punch lands on the last clause.
BIO = (
    "I've written 40,000 breakup texts for strangers and not a single "
    "one was for me. Starting to think I'm the problem."
)

MAX_CHARS = 180


def main() -> None:
    bio = BIO.strip()
    if not bio:
        raise SystemExit("bio must not be empty")
    if "\n" in bio or "\r" in bio:
        raise SystemExit("bio must be a single line")
    if len(bio) > MAX_CHARS:
        raise SystemExit(
            "bio is %d characters, over the %d limit" % (len(bio), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(bio)
    print("wrote %s (%d chars)" % (out_path, len(bio)))
    print(bio)


if __name__ == "__main__":
    main()
