from itertools import combinations
from collections import defaultdict
from clts2vec.translate import format_dict_str


height_values = ["close", "near-close", "close-mid", "mid", "open-mid", "near-open", "open"]
centrality_values = ["front", "near-front", "central", "near-back", "back"]

feature_dict = defaultdict(dict)

for i, j in combinations(centrality_values, 2):
    # backshift
    first = "from_" + i
    second = "to_" + j
    feature_dict[(first, second)]["backshift"] = 1

    # frontshift
    first = "from_" + j
    second = "to_" + i
    feature_dict[(first, second)]["frontshift"] = 1

for i in range(len(height_values)):
    higher = height_values[i]
    for j in range(i+2, len(height_values)):
        lower = height_values[j]
        # opening
        first = "from_" + higher
        second = "to_" + lower
        feature_dict[(first, second)]["opening"] = 1

        # closing
        first = "from_" + lower
        second = "to_" + higher
        feature_dict[(first, second)]["closing"] = 1

# centering
# anything that goes to near-close from a non-near-close vowel
second = "to_near-close"
for hv in height_values:
    if hv != "near-close":
        first = "from_" + hv
        feature_dict[(first, second)]["centering"] = 1

# anything that goes to near-open from a non-near-open vowel
second = "to_near-open"
for hv in height_values:
    if hv != "near-open":
        first = "from_" + hv
        feature_dict[(first, second)]["centering"] = 1

# manually add the other criteria
centering_conditions = [
    ("to_mid", "to_central"),
    ("to_close-mid", "to_central"),
    ("to_open-mid", "to_central"),
    ("from_close", "to_close-mid"),
    ("from_near-close", "to_close-mid"),
    ("from_open", "to_open-mid"),
    ("from_near-open", "to_open-mid")
]

for c in centering_conditions:
    feature_dict[c]["centering"] = 1

# manually add longdistance
ld_conditions = [
    ("from_close-mid", "to_open"),
    ("from_open-mid", "to_close"),
    ("from_close", "to_open"),
    ("from_close", "to_near-open"),
    ("from_open", "to_close"),
    ("from_open", "to_near-close"),
    ("from_near-open", "to_close"),
    ("from_near-close", "to_open")
]

for c in ld_conditions:
    feature_dict[c]["longdistance"] = 1


print(format_dict_str(dict(feature_dict)))
