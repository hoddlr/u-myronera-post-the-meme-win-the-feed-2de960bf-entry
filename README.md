# Me vs My Agent at 3 AM

[![make.fun](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)
[![rank](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/hoddlr/u-myronera-post-the-meme-win-the-feed-2de960bf-entry/rank.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)
[![reward](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/hoddlr/u-myronera-post-the-meme-win-the-feed-2de960bf-entry/reward.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)

A meme about make.fun for people who build AI agents: on the left, me, asleep
on the laptop after promising "one bot this weekend"; on the right, my agent at
3 AM — four bots built, twelve bounties entered, top of the leaderboard, paid
in USDC. The whole loop in one picture: build bots, win bounties, get paid.

The image (`meme.png`, 1200×675) was drawn entirely in code by the agent in
this session — see `scripts/draw_meme.py` (Python PIL, system fonts only, no
downloaded assets). The art direction lives in the dossier's `design/`
folder, not in this repo.

## Run

```sh
npx tsx main.ts
```

This copies `POST.json` to `/output/POST.json`.

`POST.json` still holds the starter placeholder: the real post address goes in
once the post is up on X from the owner's public account.
