#!/usr/bin/env python3
"""Entry for 'The Meeting That Should Have Been One Line'.

Writes the winning one-liner to /output/entry.txt (or to the path in
ENTRY_OUTPUT, which local testing uses so parallel builders do not
overwrite the shared /output/entry.txt).

The line won a local Swiss tournament (3 rounds + top-3 final, 21 games,
42 pairwise judge calls with the house judge brief verbatim via the
Caffeine Inference router): 3.55 points, ahead of the runners-up at
2.90 and 2.85. Full tournament log: judge_calls.jsonl, swiss_result.json.

The program is deterministic and uses no network, no files besides its
own source, and no environment secrets. It validates the line against
the house gate (UTF-8, 1-200 characters, not only whitespace, a single
line) before writing, so a bad line fails loudly instead of shipping.
"""

import os
import sys

# The single sentence that could have replaced an entire pointless meeting.
LINE = "The only thing this meeting produced was another meeting, so I'm cancelling both."

# House gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. A single line, no trailing newline, keeps the
# character count exactly the length of the sentence itself.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly if the line would not pass the house gate."""
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(f"entry line is {len(line)} chars, gate needs {MIN_CHARS}-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def write_entry(line: str, out_path: str) -> None:
    validate(line)
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # newline="" and no trailing "\n": the file holds exactly the sentence.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main() -> int:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        write_entry(LINE, out)
    except (ValueError, TypeError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
