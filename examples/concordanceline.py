from lingpy import *
from tabulate import tabulate

wl = Wordlist("../resources/nelex-europe.tsv")

spanish = []
for idx, language, concept, tokens in wl.iter_rows(
        "doculect", "concept", "tokens"):
    if language == "Spanish":
        if "m" in tokens or "ɱ" in tokens:
            spanish += [[concept, tokens]]

spanish = sorted(
        spanish,
        key=lambda x: (1 if "m" in x[1] else 0, x[0]))

# align data
cline = []
for concept, tokens in spanish:
    if "m" in tokens:
        idx = [i for i, t in zip(range(len(tokens)), tokens) if t == "m"][0]
    else:
        idx = [i for i, t in zip(range(len(tokens)), tokens) if t == "ɱ"][0]
    before, after = tokens[:idx], tokens[idx + 1:]
    cline += [[concept, " ".join(before), "red" if tokens[idx] == "m" else "darkgreen", tokens[idx], " ".join(after)]]

with open("html-representation.html", "w") as f:
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
