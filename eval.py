import sys

from clts2vec.parse import parse
from clts2vec.translate import vec_to_str
from clts2vec.features import clts_features, joint_feature_definitions
from pyclts import CLTS
from tabulate import tabulate
from collections import defaultdict

sys.path.append("src")

clts_sounds = []
clts = CLTS()

all_clts_features = defaultdict(set)  # map feature to set of values

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
    try:
        clts_sound = clts.bipa[s]
        vector = parse(clts_sound)
        # art_feature_set = vec_to_feature_set(vector)
        sounds[tuple(vector)].append(s)
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
    table += [[len(v), vec_to_str(list(k)), " ".join(v)]]
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
