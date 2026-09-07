#!/usr/bin/env python3
"""Rebuild index.html, artifact.html and CARDS.md from the JSON in data/.

Edit the JSON, run `python3 build.py`, and everything else regenerates.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
ORDER = ["word-worm", "creative-cat", "data-head", "star-performer"]
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
LETTERS = "ABCD"
out = [
    "# Cranium 2026 — every card\n",
    "Printable/scannable text of all four decks. "
    "Generated from `data/*.json` by `build.py` — edit the JSON, not this file.\n",
]
total = 0
for deck in DECKS:
    n = sum(len(a["cards"]) for a in deck["activities"])
    total += n
    out.append(f"\n## {deck['deck']} — {deck['tagline']} ({n} cards)\n")
    for act in deck["activities"]:
        out.append(f"\n### {act['name']} ({len(act['cards'])})\n")
        out.append(f"*{act['howto']}*\n")
        for i, c in enumerate(act["cards"], 1):
            if act["name"] == "Blankout":
                out.append(f"{i}. **{c['puzzle']}** — _{c['hint']}_ → {c['answer']}")
            elif act["name"] == "Gnilleps":
                out.append(f"{i}. **{c['word']}** → {c['backwards']}")
            elif act["name"] == "Spellbound":
                out.append(f"{i}. **{c['word']}**")
            elif act["name"] == "Lexicon":
                opts = "; ".join(
                    f"{LETTERS[j]}) {o}" for j, o in enumerate(c["options"])
                )
                out.append(
                    f"{i}. **{c['word']}** — {opts} → **{LETTERS[c['answer']]}**"
                )
            elif act["name"] == "Factoid":
                out.append(f"{i}. {c['q']} → **{c['a']}**")
            elif act["name"] == "Polygraph":
                verdict = "TRUE" if c["a"] else "FALSE"
                note = f" ({c['note']})" if c.get("note") else ""
                out.append(f"{i}. {c['q']} → **{verdict}**{note}")
            elif act["name"] == "Selectaquest":
                opts = "; ".join(
                    f"{LETTERS[j]}) {o}" for j, o in enumerate(c["options"])
                )
                out.append(
                    f"{i}. {c['q']} — {opts} → **{LETTERS[c['answer']]}**"
                )
            elif act["name"] == "Humdinger":
                out.append(f"{i}. **{c['clue']}** — {c['artist']}")
            else:
                out.append(f"{i}. {c['clue']}")
        out.append("")

out.insert(2, f"\n**{total} cards total.**\n")
(ROOT / "CARDS.md").write_text("\n".join(out) + "\n")
print(f"built index.html, artifact.html and CARDS.md — {total} cards")
