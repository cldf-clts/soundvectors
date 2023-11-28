from collections import defaultdict
from pyclts import CLTS


def load_features(fp):
    feature_map = defaultdict(lambda: defaultdict(list))
    flat_feature_map = defaultdict(list)

    with open(fp) as f:
        for line in f.read().split("\n"):
            line = line.split("#")[0].strip()  # cut off comments and trailing whitespaces
            if not line:
                continue
            fields = line.split()
            if len(fields) < 2:
                continue

            clts_feature = fields[0]
            clts_feat_value = fields[1]

            articulatory_features = []
            # tentative, this part should be well-defined in the tsv file later on
            if len(fields) > 2:
                articulatory_features_string = fields[2]
                if articulatory_features_string[0] == "[" and articulatory_features_string[-1] == "]":
                    articulatory_features_string = articulatory_features_string[1:-1]
                    if articulatory_features_string:
                        articulatory_features = fields[2][1:-1].split(",")

            feature_map[clts_feature][clts_feat_value] = articulatory_features
            flat_feature_map[clts_feat_value] = articulatory_features

    # collect all defined articulatory features
    features = []

    for inner_dict in feature_map.values():
        for art_feat_list in inner_dict.values():
            for art_feat in art_feat_list:
                feat_name = art_feat[1:]
                if feat_name not in features:
                    features.append(feat_name)

    return feature_map, flat_feature_map, features


f_map, flat_f_map, f_list = load_features("features/consonants.tsv")


def add_features_to_vector(feature_set, vector):
    """
    modify an existing feature vector by a given feature set.
    :param feature_set: a set of features that should be applied.
    :param vector: the feature vector to be modified.
    :return: the modified feature vector.
    """
    for feature in feature_set:
        sign = feature[0]
        name = feature[1:]
        if not ((sign == "+" or sign == "-") and name in f_list):
            continue

        feature_idx = f_list.index(name)
        if sign == "+":
            vector[feature_idx] = 1
        else:
            vector[feature_idx] = -1

    return vector


def generate_feature_vector(clts_features):
    """
    generate a feature vector from a CLTS feature bundle.
    :param clts_features: a bundle of CLTS features.
    :return: a vector representation of corresponding articulatory features.
    """
    # hierarchically sort CLTS features: sound type => primary features => secondary features
    types = ["consonant", "vowel", "diphthong", "tone"]
    base_features = ["manner", "place", "phonation"]  # currently only consonants, expand later
    base_feature_values = set()
    for f in base_features:
        base_feature_values.add(f_map[f].values())

    # put CLTS feature set in three lists (corresponding to the hierarchy above)
    present_types = []
    present_base_features = []
    present_secondary_features = []

    for feature in clts_features:
        if feature in types:
            present_types.append(feature)
        elif feature in base_feature_values:
            present_base_features.append(feature)
        else:
            present_secondary_features.append(feature)

    sorted_features = present_types + present_base_features + present_secondary_features

    # generate an empty feature vector
    feature_vector = [0] * len(f_list)

    # iterate over sorted features and modify the feature vector accordingly
    for feature in sorted_features:
        add_features_to_vector(flat_f_map[feature], feature_vector)

    return feature_vector


def vec_to_feature_set(vector):
    feature_set = set()

    for i, value in enumerate(vector):
        feature_name = f_list[i]
        if value == 1:
            feature_set.add(f"+{feature_name}")
        if value == -1:
            feature_set.add(f"-{feature_name}")

    return feature_set


if __name__ == "__main__":
    clts = CLTS()
    sounds = ["s", "t", "g", "b", "h"]

    for s in sounds:
        print(s)
        clts_features = clts.bipa[s].featureset
        print(vec_to_feature_set(generate_feature_vector(clts_features)))
        print("\n\n")
