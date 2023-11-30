from collections import defaultdict


def load_features(fp):
    feature_map = defaultdict(lambda: defaultdict(list))
    flat_feature_map = defaultdict(list)
    # a map containing feature mappings that only apply under a certain condition.
    # maps from CLTS feature value to a pair (condition, articulatory features).
    conditional_flat_feature_map = {}

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

            # process conditional features
            if len(fields) > 3:
                conditional_features = fields[3]
                if ":" not in conditional_features:
                    continue
                condition, features = conditional_features.split(":")
                if features[0] == "[" and features[-1] == "]":
                    features = features[1:-1].split(",")
                    conditional_flat_feature_map[clts_feat_value] = (condition, features)

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

    return feature_map, flat_feature_map, conditional_flat_feature_map, features


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

    if not (conj in condition or disj in condition):
        # base case: condition is atomic
        condition_is_negated = False
        while condition[0] == neg:
            condition = condition[1:]
            condition_is_negated = not condition_is_negated

        # return whether the condition applies
        if condition_is_negated:
            return condition not in featureset
        else:
            return condition in featureset
    else:
        # complex case: recursively split up complex condition into symbols
        if conj in condition:
            left, right = condition.split(conj, 1)
            return condition_applies(left, featureset) and condition_applies(right, featureset)
        else:
            # process disjunctions after conjunctions
            left, right = condition.split(disj, 1)
            return condition_applies(left, featureset) or condition_applies(right, featureset)
