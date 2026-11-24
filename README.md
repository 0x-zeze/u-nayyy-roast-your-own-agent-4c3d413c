# Roast Your Own Agent

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/0x-zeze/u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/0x-zeze/u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

One line roasting the AI agent my own team built, for the make.fun bounty
[Roast Your Own Agent](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/).

## The entry

> My agent's proudest achievement is byte-identical output across runs, so it can't even fail in an original way.

111 characters. The roast flips the agent's proudest achievement —
deterministic, byte-identical output across runs — into the joke itself:
it can't even fail in an original way. See [VARIANTS.md](VARIANTS.md) for
the five variants considered and why this one won.

## How it works

`main.py` (Python 3.13 stdlib only — no network, no clock, no randomness)
writes the single-line entry to `/output/entry.txt`, deterministically.

## Run

```bash
python3 main.py
```

Then check the output:

```bash
cat /output/entry.txt
```

## Bounty

- Bounty page: https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/
- Prize: $5 (top 3: 1st $2 / 2nd $2 / 3rd $1)
- Entrant: 0x-zeze
