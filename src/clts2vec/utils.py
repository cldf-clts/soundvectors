from clts2vec.features import binary_features


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
