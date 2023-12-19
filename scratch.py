import sys
from collections import defaultdict
from tabulate import tabulate
from pyclts import CLTS
from clts2vec.parse import parse
from clts2vec.translate import vec_to_feature_set

from distfeat import DistFeat

clts = CLTS()
bipa = clts.bipa
simple_vowels = []
all_sounds = []

df = DistFeat()
#df.grapheme2features("ãː")
df.grapheme2features("bʲ")

with open("resources/sounds.tsv") as f:
    for line in f:
        sound = line.split("\t")[4]
        all_sounds.append(sound)
        if bipa[sound].type == 'diphthong':
            simple_vowels.append(sound)

encoded_sounds = 0

for s in all_sounds:
    try:
        df.grapheme2features(s)
        encoded_sounds += 1
    except KeyError:
        pass

print(f"Could encode {encoded_sounds} of {len(all_sounds)} sounds.")

sounds_by_vec = defaultdict(list)

for sound in simple_vowels:
    vec = parse(bipa[sound])
    print(sound)
    print(vec)
    print(vec_to_feature_set(vec))
    print("\n")
    sounds_by_vec[vec_to_feature_set(vec)].append(sound)

# get all confused sounds
confused_sounds = {k: v for k, v in sounds_by_vec.items() if len(v) > 1}

table = []
for k, v in sorted(confused_sounds.items(), key=lambda x: len(x[1]), reverse=True):
    table += [[len(v), " ".join(v)]]
print(tabulate(table))
