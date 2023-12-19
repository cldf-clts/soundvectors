import sys

from clts2vec.parse import parse
from pyclts import CLTS
from tabulate import tabulate
from collections import defaultdict

sys.path.append("src")

clts_sounds = []
clts = CLTS()

header = True

with (open("resources/sounds.tsv") as f):
    for line in f:
        if header:
            header = False
            continue
        sound = line.split("\t")[4]
        sound_meta = clts.bipa[sound]

        # if (sound_meta.type == "consonant" and sound_meta.manner != "tap" and sound_meta.manner != "implosive"
         #       and (len(sound) == 1 or (sound_meta.manner == "affricate") and len(sound) == 2)):
        clts_sounds.append(sound)


sounds = defaultdict(list)
missing = 0

for s in clts_sounds:
    clts_features = clts.bipa[s].featureset
    try:
        vector = parse(clts.bipa[s])
        # art_feature_set = vec_to_feature_set(vector)
        sounds[tuple(vector)].append(s)
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
    table += [[len(v), " ".join(v)]]
print(tabulate(table))
