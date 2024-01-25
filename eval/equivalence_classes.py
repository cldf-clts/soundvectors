from clts2vec.parse import parse
from clts2vec.utils import vec_to_str
from clts2vec.features import clts_features
from pyclts import CLTS
from tabulate import tabulate
from collections import defaultdict
from csvw.dsv import UnicodeDictReader

clts_sounds = []
clts = CLTS()

all_clts_features = defaultdict(set)  # map feature to set of values

with UnicodeDictReader(clts.repos / "data" / "sounds.tsv", delimiter="\t") as reader:
    for line in reader:
        sound = line["GRAPHEME"]
        clts_sounds.append(sound)

sounds = defaultdict(list)
missing = 0

for s in clts_sounds:
    try:
        clts_sound = clts.bipa[s]
        vector = parse(clts_sound)
        sounds[vector].append(s)
        for k, v in clts_sound.featuredict.items():
            if v:
                all_clts_features[k].add(v)
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
    table += [[len(v), " ".join(v), vec_to_str(list(k))]]
print(tabulate(table))

# get CLTS features with no translation so far (aka that do not modify the feature vector)
table = []
for feature, value_set in all_clts_features.items():
    if feature.startswith("from_") or feature.startswith("to_"):
        continue
    for value in value_set:
        binary_features = clts_features.get(feature, dict()).get(value, [0])
        if set(binary_features) == {0}:
            table.append([feature, value])

print("CLTS features with null mappings:")
print(tabulate(table))
