from clts2vec.features import *


def parse(sound):
    # use the order in clts
    base_vec = clts_features["type"][sound.type].copy()
    ordered_input_features = order_features(sound.featureset)

    for feature in ordered_input_features:
        bin_feature_vec = clts_feature_values[feature]["features"]
        for k, v in bin_feature_vec.items():
            if v in [1, -1]:
                base_vec[k] = v

    base_vec = apply_joint_feature_definitions(sound, base_vec)

    # TODO secondary articulations should be applied here, not in the first loop

    return [base_vec[f] for f in binary_features]


def order_features(featureset):
    return sorted(featureset, key=lambda x: clts_feature_hierarchy.get(clts_feature_values[x]["domain"], max_hierarchy_level))


def apply_joint_feature_definitions(sound, base_vec):
    for features, bin_feature_vec in joint_feature_definitions.items():
        if set(features).issubset(sound.featureset):
            for k, v in bin_feature_vec.items():
                if v in [1, -1]:
                    base_vec[k] = v

    return base_vec
