# One Word From Grandma

[![make.fun · u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/verad-xe/grandma-word/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/verad-xe/grandma-word/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

A make.fun entry for **One Word From Grandma**
(`u-0xkianno-one-word-from-grandma-f04bed16`).
See the bounty on [make.fun](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16).

## The entry

One word — the single word Grandma would text about AI:

**thingamajig**

## Why this word

Grandma does not say "artificial intelligence". She points at the
glowing rectangle that answers back and calls it the thingamajig.
It is the word she has used for every gadget she cannot name since
before the gadget existed — the remote, the router, the thing that
makes the photos appear — and AI is only the newest thingamajig.
It is funny because it is exactly right, and it sounds like a real
text from a real grandma, not a tech word dressed up as one.

## How it works

`main.py` writes the word to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(the harness's `/output/entry.txt`). The output is exactly one word,
11 characters, UTF-8, within the required 1–30 characters.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/grandma-word-out python3 main.py
cat /tmp/grandma-word-out/entry.txt
```

## License

MIT — see `LICENSE`.
