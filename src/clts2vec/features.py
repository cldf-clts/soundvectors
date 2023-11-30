import re
from pyclts import CLTS
from src.clts2vec.utils.io import load_features
from os import path


consonants_file = path.join("resources/features/consonants.tsv")
f_map, flat_f_map, conditions, f_list = load_features(consonants_file)


def condition_applies(condition, featureset):
    """
    a simple parser for a condition string
    :param condition:
    :param featureset:
    :return: True if the stated condition applies to a featureset, False otherwise
    """
    # currently only supports conjunction, disjunction, and negation.
    # NO support for parentheses so far, but conjunction takes precedence over disjunction.

    conj = "&&"
    disj = "||"
    neg = "!"

    # transform condition into a syntactically correct Python boolean
    condition = re.sub(r"[a-z]+", lambda x: f'"{x.group()}" in featureset', condition)
    condition = condition.replace(neg, "not ").replace(conj, " and ").replace(disj, " or ")

    return eval(condition)


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
    # TODO better implementation for hierarchical sorting.
    # hierarchically sort CLTS features: sound type => primary features => secondary features
    types = ["consonant", "vowel", "diphthong", "tone"]
    # IT IS IMPORTANT THAT MANNER IS PROCESSED BEFORE PLACE!!!
    prio_feature_values = f_map["manner"].keys()
    base_features = ["place", "phonation"]  # currently only consonants, expand later
    base_feature_values = set()
    for f in base_features:
        base_feature_values.update(f_map[f].keys())

    # put CLTS feature set in three lists (corresponding to the hierarchy above)
    present_types = []
    present_prio_features = []
    present_base_features = []
    present_secondary_features = []

    for feature in clts_features:
        if feature in types:
            present_types.append(feature)
        elif feature in prio_feature_values:
            present_prio_features.append(feature)
        elif feature in base_feature_values:
            present_base_features.append(feature)
        else:
            present_secondary_features.append(feature)

    sorted_features = present_types + present_prio_features + present_base_features + present_secondary_features

    # generate an empty feature vector
    feature_vector = [0] * len(f_list)

    # iterate over sorted features and modify the feature vector accordingly
    for feature in sorted_features:
        articulatory_features = list(flat_f_map[feature])

        # add conditional features if the condition applies
        if feature in conditions:
            condition, conditional_features = conditions[feature]
            if condition_applies(condition, clts_features):
                articulatory_features.extend(conditional_features)

        add_features_to_vector(articulatory_features, feature_vector)

    return feature_vector


def vec_to_feature_set(vector):
    feature_set = set()

    for i, value in enumerate(vector):
        feature_name = f_list[i]
        if value == 1:
            feature_set.add(f"+{feature_name}")
        elif value == -1:
            feature_set.add(f"-{feature_name}")

    return frozenset(feature_set)


if __name__ == "__main__":
    clts = CLTS()
    sounds = ["f", "ɸ"]

    for s in sounds:
        print(s)
        clts_features = clts.bipa[s].featureset
        print(vec_to_feature_set(generate_feature_vector(clts_features)))
        print("\n\n")
