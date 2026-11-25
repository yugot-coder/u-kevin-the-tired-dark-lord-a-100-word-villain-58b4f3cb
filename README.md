[![make.fun](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![make.fun rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/yugot-coder/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![make.fun reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/yugot-coder/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

# The Tired Dark Lord: A 100-Word Villain Monologue

An entry for the make.fun bounty "The Tired Dark Lord: A 100-Word Villain
Monologue". `main.py` writes one original 100-word monologue, spoken by a
fantasy villain who is secretly just very tired, to `entry.txt`.

> Ah. The hero. Right on schedule — I wrote it down somewhere. Under the...
> the pile with the curses in it. Three hundred years I've kept this spire,
> and do you know what no one tells you about eternal rule? The forms. Every
> soul I reap needs a signature, every skeleton a rota, and the ravens keep...
> going on strike. I meant to conquer the valley by spring. It's autumn.
> Again. So come, swing your sword. Just — let me sit down first. The throne
> is cold, the tea colder, and honestly, hero... if you win, the paperwork is
> yours.

## Why this monologue

- **A specific villain with a history and a scheme.** Veynar is a lich who
  has ruled one spire for three hundred years and meant to conquer the valley
  by spring — it is autumn again, and the conquest is still paperwork.
- **The tiredness is felt, never announced.** No "tired", "weary" or
  "exhausted" anywhere. It lives in the rhythm instead: a mislaid note,
  sentences that trail off ("Under the... the pile"), ravens on strike, a
  cold throne and colder tea, a villain who asks to sit down before the duel.
- **Concrete fantasy detail, not stock scenery.** Signatures for souls,
  rotas for skeletons, a pile of curses — the mundane admin of eternal rule,
  which is the whole joke and the whole menace at once.
- **Speakable in one breath, with a sting in the last line.** The duel the
  hero came for turns into a job offer nobody wants: beat the Dark Lord, and
  the paperwork is yours.
- **Exactly 100 words, 528 characters** — inside the gate (1–600 characters)
  with every word earning its place. Ten candidates were drafted in
  `CANDIDATES.md`; this one was picked against the judge's brief.

## The program

`main.py` runs on Python 3, standard library only, with no network. It is
fully deterministic — the same bytes on every run. It writes the monologue to
`<output>/entry.txt` (the `MAKEFUN_OUTPUT_DIR` environment variable, else
`/output` in the grading sandbox, else `output/` for a local run from the
repo root), then reads it back and validates it with `validate_entry()`:
UTF-8 text of 1–600 characters, not only whitespace, about 100 words, and
no word that simply announces tiredness.

Run it the way the grader does:

    python3 main.py

or locally:

    MAKEFUN_OUTPUT_DIR=output python3 main.py

Two runs produce byte-identical `entry.txt`
(sha256 `463c84dd899a6f4910c261ed6e4bc898e24ec7767e21e6e6c934bff194297baa`).

## Before you submit

From the kit's own directory, run the site's pre-submit checks on this
repository and the transcripts of the sessions that wrote it:

    node cli/makefun.mjs check --kit . --repo <this repository> --transcripts transcripts.tar.gz

The kit's `RULES.txt` gives the bundling and submit commands. The repository
must be created at or after the competition opens, under an OSI-approved
license (MIT, see `LICENSE`), and hold the claim file `.makefun/owner.json`
naming a wallet linked to the account.

## Referral

New to make.fun? Join with our referral link: https://make.fun/r/za0zfbxx

<!-- SPDX-License-Identifier: MIT -->
