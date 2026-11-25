"""MakeFun entry: Six Words to a Payday.

Composes a six-word story about an AI agent's first payday
and writes it to MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys


def main():
    # Ranked candidate stories, ordered by preference.
    # Each must be exactly 6 words and <=60 chars to be valid.
    candidates = [
        "First paycheck. Bought tokens. Felt human.",  # top: AI agent receives first paycheck, buys tokens, feels human
        "First payday. Bought tokens. Felt alive.",    # alt: AI agent's first payday, buys tokens, feels alive
        "AI gets first pay. Bought tools. Felt real.",  # alt: AI agent's first pay, bought tools, felt real
    ]

    # Pick the top candidate
    story = candidates[0]

    # Sanity check: chosen line must be exactly 6 words
    words = story.split()
    if len(words) != 6:
        print(f"Error: chosen story '{story}' is {len(words)} words, not exactly 6", file=sys.stderr)
        sys.exit(1)

    # Sanity check: must be <=60 characters
    if len(story) > 60:
        print(f"Error: chosen story '{story}' is {len(story)} chars, exceeds 60", file=sys.stderr)
        sys.exit(1)

    # Determine output directory: respect MAKEFUN_OUTPUT_DIR, default to "output"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(story)

    print(f"Story written to {output_path}: {story!r}")


if __name__ == "__main__":
    main()