# Cranium 2026

The original Cranium came out in 1998, and it shows — half the prompts are 80s and 90s
references nobody at the table recognizes anymore. This is a drop-in replacement set of
prompts written for right now.

**How you play:** draw a real card from the box, read off which deck and card type it is
(say, Word Worm → Blankout), then play one of *these* Blankouts instead. Every rule, the
timer, and the board stay exactly the same. Only the prompts change.

**390 cards** across the four decks, matching the game's real card types:

| Deck | Card types |
| --- | --- |
| **Word Worm** — spelling and wordplay | Blankout, Gnilleps, Lexicon, Spellbound |
| **Creative Cat** — draw and sculpt | Cloodle, Sensosketch, Sculptorades |
| **Data Head** — trivia | Factoid, Polygraph, Selectaquest |
| **Star Performer** — acting | Cameo, Copycat, Humdinger |

Thirty cards per type.

## Using it at game night

- **[`index.html`](index.html)** — open it in any browser (phone included). Tap a deck, tap
  a card type, and it deals. Each type shuffles its own pile, so you see all thirty before
  anything repeats. There's a 60-second timer built in to match the sand timer in the box.
- **[`CARDS.md`](CARDS.md)** — the whole set as plain text, if you'd rather print it or
  read off a page.

Keyboard shortcuts while playing: <kbd>N</kbd> deals the next card, <kbd>A</kbd> shows the
answer, <kbd>T</kbd> starts and stops the timer.

## What each card type asks for

**Word Worm**
- *Blankout* — a word or phrase with letters missing; the team fills them in.
- *Gnilleps* — spell the word backwards, out loud.
- *Lexicon* — pick the right definition out of three.
- *Spellbound* — spell the word, forwards.

**Creative Cat**
- *Cloodle* — draw it, eyes open.
- *Sensosketch* — draw it with your eyes closed.
- *Sculptorades* — sculpt it out of clay.

**Data Head**
- *Factoid* — a straight trivia question.
- *Polygraph* — true or false.
- *Selectaquest* — multiple choice.

**Star Performer**
- *Cameo* — charades, silent.
- *Copycat* — impersonate them out loud, without saying the name.
- *Humdinger* — hum the tune, no words.

## Editing the decks

The cards live in `data/*.json` — one file per deck, each with its card types and their
cards. Add, cut, or reword whatever you like, then run:

```
python3 build.py
```

That regenerates `index.html`, `artifact.html`, and `CARDS.md` from the JSON.
`template.html` is the page itself; `build.py` just injects the card data into it.

A note on the trivia: Data Head answers were correct as of 2026. A few (streaming
catalogs, who owns what) will drift — fix them in `data/data-head.json` and rebuild.
