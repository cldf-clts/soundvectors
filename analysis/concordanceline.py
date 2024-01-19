from lingpy import *
from pathlib import Path
from tabulate import tabulate

wl = Wordlist.from_cldf(Path(__file__).parent.parent / "resources/eval/northeuralex/cldf/cldf-metadata.json")

colors = ["red", "darkgreen", "darkblue"]

### DECLARE IMPORTANT INFORMATION HERE ###
lang = "ekk"
sounds = ["k", "g̊", "k̥"]
##########################################


relevant_forms = []
for idx, language, concept, tokens in wl.iter_rows(
        "doculect", "concept", "tokens"):
    if language == lang:
        if set(tokens).intersection(set(sounds)):
            relevant_forms += [[concept, tokens]]

# align data
cline = []
for concept, tokens in relevant_forms:
    for i, t in enumerate(tokens):
        if t in sounds:
            before, after = tokens[:i], tokens[i + 1:]
            cline += [[concept, " ".join(before), colors[sounds.index(t)], t, " ".join(after)]]

cline = sorted(
        cline,
        key=lambda x: (sounds.index(x[3]), x[0]))

outfile = Path(__file__).parent / f"clines/{lang}.html"

with open(outfile, "w") as f:
    f.write('<html><meta charset="utf-8"><body>')
    f.write("<table>")
    for a, b, c, d, e in cline:
        f.write("""
<tr>
<th style="text-align:left">{0}</th>
<td style="text-align:right">{1}</td>
<td style="background-color:{2}; color:white;align:center">{3}</td>
<td>{4}</td>
                </tr>""".format(a, b, c, d, e))
    f.write("</table></body></html>")
