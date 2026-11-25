#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — entry for make.fun.

Competition: u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

Writes one original 100-word monologue (528 characters) spoken by Veynar,
a lich who has ruled his spire for three hundred years and is secretly just
very tired, to <output>/entry.txt.

Standard library only. Deterministic: the same bytes on every run.
No network, no randomness, no input files.

The tiredness lives in the voice, not in a label: trailing thoughts, a
mislaid note, a strike, a cold throne, a colder cup of tea. The villain
never says he is weary. The last line turns the whole duel around.
"""

import os

MONOLOGUE = (
    "Ah. The hero. Right on schedule \u2014 I wrote it down somewhere. "
    "Under the... the pile with the curses in it. Three hundred years "
    "I've kept this spire, and do you know what no one tells you "
    "about eternal rule? The forms. Every soul I reap needs a "
    "signature, every skeleton a rota, and the ravens keep... going "
    "on strike. I meant to conquer the valley by spring. It's "
    "autumn. Again. So come, swing your sword. Just \u2014 let me sit "
    "down first. The throne is cold, the tea colder, and honestly, "
    "hero... if you win, the paperwork is yours."
)


def validate_entry(text):
    """Check the monologue against the gate in RULES.txt and the judge
    brief: UTF-8 text of 1 to 600 characters, not only whitespace, about
    100 words, and the tiredness never announced outright."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    if not 1 <= len(text) <= 600:
        raise ValueError(f"length {len(text)} outside the 1-600 gate")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    words = text.split()
    if not 90 <= len(words) <= 110:
        raise ValueError(f"expected about 100 words, got {len(words)}")
    lowered = text.lower()
    for announced in ("tired", "weary", "exhausted", "sleep-deprived"):
        if announced in lowered:
            raise ValueError(f"entry announces its tiredness: {announced!r}")
    return len(words)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir is None:
        # The grader runs in a sandbox with /output; a plain local run
        # from the repo root writes to the relative output/ directory.
        out_dir = "/output" if os.path.isdir("/output") else "output"
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)
    # Read-back validation: fail loudly here rather than shipping a bad file.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == MONOLOGUE, "entry.txt does not match the monologue"
    word_count = validate_entry(written)
    print(f"validated: {word_count} words, {len(written)} chars, "
          f"no announced tiredness")
    print(f"wrote {len(written)} chars to {out_path}")


if __name__ == "__main__":
    main()
