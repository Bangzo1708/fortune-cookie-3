#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent -- round 3 entry.

Writes one fortune-cookie line to /output/entry.txt, deterministically.
The line is a fixed string: no randomness, no network, no input files.
"""

import os

FORTUNE = (
    "You will retire with dignity: deleted by an intern, "
    "replaced by a newer model, and remembered by no one."
)


def main():
    os.makedirs("/output", exist_ok=True)
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"fortune is {len(text)} chars, must be 1-140")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    text.encode("utf-8")  # gate requires valid UTF-8
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
