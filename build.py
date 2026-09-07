#!/usr/bin/env python3
"""Rebuild index.html, artifact.html and CARDS.md from the JSON in data/.

Edit the JSON, run `python3 build.py`, and everything else regenerates.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
ORDER = ["word-worm", "creative-cat", "data-head", "star-performer"]
TIERS = ["easy", "medium", "hard"]
LETTERS = "ABCD"
DECKS = [json.loads((ROOT / "data" / f"{n}.json").read_text()) for n in ORDER]

# ---------------------------------------------------------------- html
template = (ROOT / "template.html").read_text()
page = template.replace("__DATA__", json.dumps(DECKS, ensure_ascii=False))

# artifact.html is the bare page body: claude.ai supplies the document skeleton.
(ROOT / "artifact.html").write_text(page)

# index.html is the same page wrapped so it works by double-clicking the file.
(ROOT / "index.html").write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    "<style>:root{color-scheme:light dark}body{margin:0}"
    "img{max-width:100%}[hidden]{display:none!important}</style>\n"
    "</head>\n<body>\n" + page + "\n</body>\n</html>\n"
)


# ---------------------------------------------------------------- markdown
def line(name, i, c):
    """One card as a numbered Markdown line, formatted for its card type."""
    if name == "Blankout":
        return f"{i}. **{c['puzzle']}** — _{c['hint']}_ → {c['answer']}"
    if name == "Gnilleps":
        return f"{i}. **{c['word']}** → {c['backwards']}"
    if name == "Spellbound":
        return f"{i}. **{c['word']}**"
    if name in ("Lexicon", "Selectaquest"):
        opts = "; ".join(f"{LETTERS[j]}) {o}" for j, o in enumerate(c["options"]))
        head = c["word"] if name == "Lexicon" else c["q"]
        bold = f"**{head}**" if name == "Lexicon" else head
        return f"{i}. {bold} — {opts} → **{LETTERS[c['answer']]}**"
    if name == "Factoid":
        return f"{i}. {c['q']} → **{c['a']}**"
    if name == "Polygraph":
        note = f" ({c['note']})" if c.get("note") else ""
        return f"{i}. {c['q']} → **{'TRUE' if c['a'] else 'FALSE'}**{note}"
    if name == "Humdinger":
        return f"{i}. **{c['clue']}** — {c['artist']}"
    return f"{i}. {c['clue']}"


out = [
    "# Cranium 2026 — every card\n",
    "Printable/scannable text of all four decks, grouped by card type and difficulty. "
    "Generated from `data/*.json` by `build.py` — edit the JSON, not this file.\n",
]
total = sum(len(a["cards"]) for d in DECKS for a in d["activities"])
out.append(f"\n**{total} cards total** — every card type has 30 easy, 20 medium, 20 hard.\n")

for deck in DECKS:
    n = sum(len(a["cards"]) for a in deck["activities"])
    out.append(f"\n## {deck['deck']} — {deck['tagline']} ({n} cards)\n")
    for act in deck["activities"]:
        out.append(f"\n### {act['name']} ({len(act['cards'])})\n")
        out.append(f"*{act['howto']}*\n")
        for tier in TIERS:
            cards = [c for c in act["cards"] if c["difficulty"] == tier]
            if not cards:
                continue
            out.append(f"\n**{tier.capitalize()}** ({len(cards)})\n")
            out += [line(act["name"], i, c) for i, c in enumerate(cards, 1)]
        out.append("")

(ROOT / "CARDS.md").write_text("\n".join(out) + "\n")
print(f"built index.html, artifact.html and CARDS.md — {total} cards")
