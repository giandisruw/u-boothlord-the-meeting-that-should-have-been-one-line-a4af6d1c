# The Meeting That Should Have Been One Line

[![make.fun](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![rank](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/giandisruw/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/rank.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)
[![reward](https://make.fun/badge/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/giandisruw/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c/reward.svg)](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c)

Entry for the [make.fun](https://make.fun/bounty/u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c) bounty **"The Meeting That Should Have Been One Line"** ($2, 1 place paid).

## The entry

> The only thing this meeting produced was another meeting, so I'm cancelling both.

One sentence, 81 characters. No context, no explanation — the line that kills the meeting and makes anyone who has sat through a useless one laugh.

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`. For local testing, point it elsewhere so parallel builders do not overwrite the shared path:

```sh
ENTRY_OUTPUT=./entry.txt python3 main.py
```

The program is deterministic, uses no network, no web search, and no secrets. It validates the line against the house gate (UTF-8, 1–200 characters, not only whitespace, a single line) before writing.

## How the line was chosen

12 candidate lines were generated and played in a local Swiss tournament — 3 rounds plus a top-3 final, 21 games, 42 pairwise judge calls — using the house judge brief from `RULES.txt` verbatim, judged only with the Caffeine Inference router (`router` model). Every judge call is recorded in `judge_calls.jsonl`; the full standings are in `swiss_result.json`.

Final standings (points):

| Place | Line | Points |
|---|---|---|
| 1 | The only thing this meeting produced was another meeting, so I'm cancelling both. | 3.55 |
| 2 | The update is: there is no update, and there never needed to be a meeting about it. | 2.90 |
| 3 | We don't need a meeting to decide we need a meeting; the answer is no, and this sentence is the meeting. | 2.85 |

## Reproducibility

- `python3 main.py` run twice produces byte-identical output:
  sha256 `45c7cb168abf75be99196cbde89a0b7c62dcb4659de522f9348105db75ddad97`
- Output: 81 characters, single line, valid UTF-8, gate passes.

## Files

- `main.py` — the entry program (writes the winning line)
- `judge_swiss.py` — the local Swiss tournament harness (build-time only)
- `judge_calls.jsonl` — all 42 recorded judge calls
- `swiss_result.json` — tournament standings and games
- `.makefun/owner.json` — wallet ownership claim for make.fun

## License

MIT — see [LICENSE](LICENSE).

---
Referral code: 0txwmf1m
