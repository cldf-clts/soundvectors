from soundvectors import SoundVectors, FeatureBundle
from pyclts import CLTS
from tabulate import tabulate
from collections import defaultdict
from csvw.dsv import UnicodeDictReader

clts_sounds = []
clts = CLTS()

sv = SoundVectors(ts=clts.bipa)

with UnicodeDictReader(clts.repos / "data" / "sounds.tsv", delimiter="\t") as reader:
    for line in reader:
        sound = line["GRAPHEME"]
        clts_sounds.append(sound)

sounds = defaultdict(list)
processed = 0
missing = 0

for s in clts_sounds:
    processed += 1
    try:
        clts_sound = clts.bipa[s]
        vector = sv.get_vec(clts_sound)
        sounds[vector].append(s)
    except:
        missing += 1


total = len(clts_sounds)

print(f"Feature table can encode {total - missing} of {total} sounds ({missing} missing).")

table = [
    ["Parsed Sounds", total - missing],
    ["Unique Sounds", len(sounds)]
]
print(tabulate(table))

# get all confused sounds
confused_sounds = {k: v for k, v in sounds.items() if len(v) > 1}

table = []
for k, v in sorted(confused_sounds.items(), key=lambda x: len(x[1]), reverse=True)[:20]:
    features = FeatureBundle(**dict(zip([f.name for f in FeatureBundle.fields()], k)))
    table += [[len(v), " ".join(v), str(features)]]
print(tabulate(table))
