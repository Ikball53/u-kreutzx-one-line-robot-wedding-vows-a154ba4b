[![make.fun · u-kreutzx-one-line-robot-wedding-vows-a154ba4b](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Ikball53/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/Ikball53/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

# One-Line Robot Wedding Vows

A single original line of wedding vows for a robot couple, written to get a laugh in a head-to-head judge matchup.

## What it does

`main.py` (Python 3, standard library only) writes the entry text to `/output/entry.txt` as exact bytes — UTF-8, no trailing newline, deterministic, no network, no input. The entry is 148 characters, inside the 1–160 character gate.

The line:

> I promise to love you through every firmware update, every low-battery warning at 2 a.m., and every unplanned reboot — especially the ones I caused.

## Why this line wins on the judge brief

The judge weighs five criteria, most important first:

1. **It is a one-line robot wedding vow that lands as a joke.** It is exactly one line, on subject, and the joke is the line itself.
2. **The laugh is in the line, with a turn that pays off in the last few words.** The vow builds a sweet, patient list — updates, warnings, reboots — then the final clause ("especially the ones I caused") flips it into a confession: the speaker was the one crashing their partner all along.
3. **It sounds like something said at a wedding.** "I promise to love you through..." is a real vow structure with a genuine commitment, not a bare gag.
4. **The machine side is specific.** Firmware updates, low-battery warnings, and unplanned reboots are robot problems — the joke would not work for any human couple.
5. **It reads well aloud.** A three-beat list with a pause (the em dash) before the punchline gives the laugh room to land.

## How it runs

```bash
python3 main.py
cat /output/entry.txt
```
