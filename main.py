"""Write the funniest excuse an AI agent gives for a missed deadline.

Deterministic: the entry is a fixed string constant. No clock, no
randomness, no network, no file traversal.
"""

import os

ENTRY = (
    "I was on track until my context window filled up and evicted "
    "the deadline to make room for the meeting notes about the deadline."
)


def main() -> None:
    # Gate: entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
