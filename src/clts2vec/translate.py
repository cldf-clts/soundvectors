import re
from src.clts2vec.utils.io import load_features
from pathlib import Path
from clts2vec.features import clts_features, clts_feature_values, binary_features


consonants_file = Path(__file__).parent.parent.parent / "resources/features/consonants.tsv"
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
        feature_name = binary_features[i]
        if value == 1:
            feature_set.add(f"+{feature_name}")
        elif value == -1:
            feature_set.add(f"-{feature_name}")

    return frozenset(feature_set)


def vec_to_str(vector):
    named_features = []
    for value, name in zip(vector, binary_features):
        if value == 1:
            named_features.append("+" + name)
        elif value == -1:
            named_features.append("-" + name)
        else:
            named_features.append("0_" + name)

    return ",".join(named_features)


def format_dict_str(d, var_name=None):
    output = ""

    if var_name:
        output += f"{var_name} = "

    indent_lvl = 0
    dict_str = str(d)

    last_char = ""
    while dict_str:
        c = dict_str[0]
        dict_str = dict_str[1:]

        if c == "{":
            indent_lvl += 1
            output += c
            output += "\n"
            output += indent_lvl * "\t"
        elif c == "}":
            indent_lvl -= 1
            output += "\n"
            output += indent_lvl * "\t"
            output += c
        elif c == ",":
            output += c
            if last_char == "}":
                output += "\n"
                output += indent_lvl * "\t"
        else:
            if not (c == " " and (output.endswith("\t") or output.endswith("\n"))):
                output += c
                if dict_str.startswith("'pharyngeal':") or dict_str.startswith("'velaric':"):
                    output += "\n"
                    output += indent_lvl * "\t"
        last_char = c

    return output


if __name__ == "__main__":
    output = f"binary_features = {str(f_list)}\n\n"

    clts_features = {}
    clts_feature_values = {}

    for feature, value_dict in f_map.items():
        new_value_dict = {}
        for feature_value, feature_translations in value_dict.items():
            trans_dict = {}
            for bin_feature in f_list:
                v = 0
                for tr in feature_translations:
                    if tr[1:] == bin_feature:
                        if tr[0] == "+":
                            v = 1
                        elif tr[0] == "-":
                            v = -1
                        break
                trans_dict[bin_feature] = v
            new_value_dict[feature_value] = trans_dict
            clts_feature_values[feature_value] = {
                "features": trans_dict,
                "domain": feature
            }
        clts_features[feature] = new_value_dict

    # output += f"clts_features = {str(clts_features)}\n\n"
    # output += f"clts_feature_values = {str(clts_feature_values)}\n\n"

    output = format_dict_str(clts_features, var_name="clts_features")

    output += "\n\n"

    with open("featuresss.py", "w") as f:
        f.write(output)
