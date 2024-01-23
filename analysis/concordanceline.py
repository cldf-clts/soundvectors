from lingpy import *
from pathlib import Path
from tqdm import tqdm
from pyclts import CLTS
from tabulate import tabulate

wl = Wordlist.from_cldf(Path(__file__).parent.parent / "resources/eval/lexibank-analysed/cldf/wordlist-metadata.json")
print("Loaded data.")

colors = ["red", "darkgreen", "darkblue"]

bipa = CLTS().bipa

### DECLARE IMPORTANT INFORMATION HERE ###
langs = ['johanssonsoundsymbolic-Alsea', 'naganorgyalrongic-JinchuanGuaninqiaorGyalrong', 'naganorgyalrongic-NyagrongMinyag', 'sagartst-Daofu', 'sagartst-Lhasa', 'sagartst-Xiandao', 'sagartst-Zhaba', 'suntb-Trung', 'yangyi-Kuansi']
sounds = ["ç", "ɕ"]
sounds = [bipa[s] for s in sounds]
##########################################


relevant_forms = []
for idx, language, concept, tokens in tqdm(wl.iter_rows(
        "doculect", "concept", "tokens")):
    if language in langs:
        tokens = [bipa[s] for s in tokens]
        if set(tokens).intersection(set(sounds)):
            relevant_forms += [[language, concept, tokens]]

# align data
cline = []
for language, concept, tokens in relevant_forms:
    for i, t in enumerate(tokens):
        if t in sounds:
            before, after = tokens[:i], tokens[i + 1:]
            cline += [[language, concept, " ".join(before), colors[sounds.index(t)], t, " ".join(after)]]

cline = sorted(
        cline,
        key=lambda x: (x[0], sounds.index(x[4]), x[1]))

outfile = Path(__file__).parent / f"clines/palat/unvoiced_fricatives.html"

with open(outfile, "w") as f:
    f.write('<html><meta charset="utf-8"><body>')
    f.write("<table>")
    for lang, concept, before, color, token, after in cline:
        f.write(f"""
<tr>
<th style="text-align:left">{lang}</th>
<th style="text-align:left">{concept}</th>
<td style="text-align:right">{before}</td>
<td style="background-color:{color}; color:white;align:center">{token}</td>
<td>{after}</td>
                </tr>""")
    f.write("</table></body></html>")
