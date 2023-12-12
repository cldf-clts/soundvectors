from collections import defaultdict
from tabulate import tabulate
from pyclts import CLTS
from clts2vec.parse import parse
from clts2vec.translate import vec_to_feature_set

bipa = CLTS().bipa
simple_vowels = []

with open("resources/sounds.tsv") as f:
    for line in f:
        sound = line.split("\t")[4]
        if bipa[sound].type == 'tone':
            simple_vowels.append(sound)

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
