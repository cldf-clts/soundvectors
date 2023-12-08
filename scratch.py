from pyclts import CLTS
from clts2vec.parse import parse
from clts2vec.translate import vec_to_feature_set


bipa = CLTS().bipa

for sound in ["p", "t", "k", "pʰ", "f", "fʰ", "ʔ"]:
    vec = parse(bipa[sound])
    print(sound)
    print(vec)
    print(vec_to_feature_set(vec))
    print("\n")
