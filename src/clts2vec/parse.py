from clts2vec.features import *


def parse(sound, vectorize=True):
    base_vec = {f: 0 for f in binary_features}
    primary_features, secondary_features = get_primary_and_secondary_features(sound.featureset)

    for feature in primary_features:
        base_vec = apply_feature(feature, base_vec)

    # diphthongs take their core vowel features from their first vowel,
    # diphthong-specific features are then applied afterwards
    if sound.type == "diphthong":
        base_vec = parse(sound.from_sound, vectorize=False)

    base_vec = apply_joint_feature_definitions(sound, base_vec)

    for feature in secondary_features:
        base_vec = apply_feature(feature, base_vec)

    if not vectorize:
        return base_vec

    return [base_vec[f] for f in binary_features]


def order_features(featureset):
    return sorted(featureset, key=lambda x: clts_feature_hierarchy.get(
        clts_feature_values.get(x, {"domain": ""})["domain"], max_hierarchy_level))


def get_primary_and_secondary_features(featureset):
    primary_features, secondary_features = [], []

    for feature in featureset:
        if clts_feature_values.get(feature, {"domain": ""})["domain"] in clts_feature_hierarchy:
            primary_features.append(feature)
        else:
            secondary_features.append(feature)

    return order_features(primary_features), secondary_features


def apply_feature(feature, base_vec):
    bin_feature_vec = clts_feature_values.get(feature, {"features": {}})["features"]
    for k, v in bin_feature_vec.items():
        if v in [1, -1]:
            base_vec[k] = v

    return base_vec


def apply_joint_feature_definitions(sound, base_vec):
    for features, bin_feature_vec in joint_feature_definitions.items():
        if set(features).issubset(sound.featureset):
            for k, v in bin_feature_vec.items():
                if v in [1, -1]:
                    base_vec[k] = v

    return base_vec
