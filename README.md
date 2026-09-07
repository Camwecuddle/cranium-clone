# Cranium 2026

The original Cranium came out in 1998, and it shows — half the prompts are 80s and 90s
references nobody at the table recognizes anymore. This is a drop-in replacement set of
prompts written for right now.

**How you play:** draw a real card from the box, read off which deck and card type it is
(say, Word Worm → Blankout), then play one of *these* Blankouts instead. Every rule, the
timer, and the board stay exactly the same. Only the prompts change.

**1,170 cards** across the four decks, matching the game's real card types:

| Deck | Card types |
| --- | --- |
| **Word Worm** — spelling and wordplay | Blankout, Gnilleps, Lexicon, Spellbound |
| **Creative Cat** — draw and sculpt | Cloodle, Sensosketch, Sculptorades |
| **Data Head** — trivia | Factoid, Polygraph, Selectaquest |
| **Star Performer** — acting | Cameo, Copycat, Humdinger |

Every card type has **90 cards in three difficulty tiers** — 40 easy, 25 medium, 25 hard.

## What era the references come from

Most people playing are somewhere in their twenties, so the cards are aimed at what that
group actually shares: roughly **2008 through today**. That means the current stuff (AI,
Ozempic, *The Bear*, Sabrina Carpenter) sits alongside the things they grew up on — Vine,
Club Penguin, Guitar Hero, the Wii, LimeWire, 2010s pop, the first iPhone. A table of
25-year-olds should recognize a card from either end.

Difficulty means something different for each card type, so each one scales on its own
axis rather than just getting longer:

| Card type | Easy | Hard |
| --- | --- | --- |
| Blankout | About a third of the letters showing, on something famous | Almost no letters showing, on a term you have to actually know |
| Gnilleps | 7–9 letters | 12–16 letters, with ugly consonant runs |
| Lexicon | Terms you've seen but couldn't define exactly | Obscure terms where all three definitions sound plausible |
| Spellbound | Commonly misspelled words | Silent letters and foreign spellings — `MILLEFEUILLE`, `PARALLELEPIPED`, `SYZYGY` |
| Cloodle / Sensosketch / Sculptorades | A concrete object | An abstract concept — *burnout*, *the attention economy* |
| Cameo / Copycat | A simple physical bit | Abstractions — *déjà vu*, *compound interest*, *the last slice of pizza* |
| Factoid / Selectaquest | General knowledge | Dates, figures, and specifics |
| Polygraph | Obviously true or obviously false | Counterintuitive facts and believable falsehoods |
| Humdinger | Hooks everybody knows | Film scores, game themes, and the Netflix *ta-dum* |

Easy is not a different game — it's the same game with a fair chance of getting it. A
Lexicon card should still be close to a coin flip the way the original's were; if your
table is guessing every easy card correctly, something is miscalibrated and worth
retuning in the JSON.

Mixing tiers works well as a handicap: put the people who play a lot on hard and everyone
else on easy.

Every clue in the drawing, sculpting, and acting decks is a short, nameable thing — five
words at most — so the guessing team has something exact to land on rather than a scene
they have to narrate back word for word.

## Using it at game night

- **[`index.html`](index.html)** — open it in any browser (phone included). Tap a deck, a
  card type, and a difficulty, and it deals. Each combination shuffles its own pile, so you
  see everything in it before anything repeats. There's a 60-second timer built in to match
  the sand timer in the box.
- **[`CARDS.md`](CARDS.md)** — the whole set as plain text, if you'd rather print it or
  read off a page.

Keyboard shortcuts while playing: <kbd>N</kbd> deals the next card, <kbd>A</kbd> shows the
answer, <kbd>T</kbd> starts and stops the timer, and <kbd>1</kbd> <kbd>2</kbd> <kbd>3</kbd>
jump to easy, medium, and hard (<kbd>0</kbd> for any tier).

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
cards. Every card carries a `"difficulty"` of `easy`, `medium`, or `hard`. Add, cut, or
reword whatever you like, then run:

```
python3 build.py
```

That regenerates `index.html`, `artifact.html`, and `CARDS.md` from the JSON.
`template.html` is the page itself; `build.py` just injects the card data into it.

A note on the trivia: Data Head answers were correct as of 2026. A few (streaming
catalogs, who owns what) will drift — fix them in `data/data-head.json` and rebuild.
