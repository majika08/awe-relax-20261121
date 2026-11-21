"""Warm Soup, Winter Night — make.fun awe (relax text) entry.

Writes one short text to /output/entry.txt: a cold winter night outside,
a room warmed by a fireplace, warm soup in both hands — and a closing line
that opens back out to the large stillness, so the calm keeps growing
after the last line. Deterministic: the same lines, joined the same way,
every run.
"""

LINES = [
    "Outside, snow falls on snow, and the night is wide and still.",
    "Inside, the fire ticks low, and soup steams in both hands.",
    "The spoon is warm, the bread is warm, the room smells of woodsmoke.",
    "Nothing asks for anything. The fire ticks. The snow falls. The night goes on.",
]


def build_text() -> str:
    """Assemble the text from its lines, in order, no padding."""
    return "\n".join(line for line in LINES if line.strip())


def main() -> None:
    import os

    text = build_text()
    # The gate requires 1-280 Unicode code points, not only whitespace.
    # Verified locally: this text is 266 code points, 266 bytes.
    if not (1 <= len(text) <= 280) or not text.strip():
        raise ValueError(f"text length {len(text)} out of range 1-280")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
