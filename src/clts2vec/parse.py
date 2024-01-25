from clts2vec.features import *
from pyclts import CLTS
from pathlib import Path

__all__ = ["parse", "PATH_TO_CLTS"]
PATH_TO_CLTS = Path(__file__).parent.parent.parent / "clts"


def parse(sound, vectorize=True):
    # if a string is passed, try analyzing it as an IPA symbol.
    if isinstance(sound, str):
        sound = CLTS(PATH_TO_CLTS).bipa[sound]

    base_vec = {f: 0 for f in binary_features}
    primary_features, secondary_features = __get_primary_and_secondary_features(sound.featureset)

    for feature in primary_features:
        base_vec = __apply_feature(feature, base_vec)

    # diphthongs take their core vowel features from their first vowel,
    # diphthong-specific features are then applied afterwards
    if sound.type == "diphthong":
        base_vec = parse(sound.from_sound, vectorize=False)
        # assign [+long] if second part of the diphthong is long
        if sound.to_sound.duration:
            base_vec = __apply_positive_features(sound.to_sound.duration, base_vec)
        # assign [+nas] if second part of the diphthong is nasalized
        if sound.to_sound.nasalization:
            base_vec = __apply_positive_features(sound.to_sound.nasalization, base_vec)
    elif sound.type == "cluster":
        from_vec = parse(sound.from_sound, vectorize=False)
        to_vec = parse(sound.to_sound, vectorize=False)
        for f in binary_features:
            if from_vec[f] == 1 or to_vec[f] == 1:
                base_vec[f] = 1
            elif from_vec[f] == -1 or to_vec[f] == -1:
                base_vec[f] = -1
            else:
                base_vec[f] = 0

    base_vec = __apply_joint_feature_definitions(sound, base_vec)

    for feature in secondary_features:
        base_vec = __apply_feature(feature, base_vec)

    if not vectorize:
        return base_vec

    return tuple([base_vec[f] for f in binary_features])


def __order_features(featureset):
    return sorted(featureset, key=lambda x: clts_feature_hierarchy.get(
        clts_feature_values.get(x, {"domain": ""})["domain"], max_hierarchy_level))


def __split_compound_features(featureset):
    split_features = []

    for f in featureset:
        split_features.extend(f.split("-and-"))

    return split_features


def __get_primary_and_secondary_features(featureset):
    # split compound features first
    featureset = __split_compound_features(featureset)

    primary_features, secondary_features = [], []

    for feature in featureset:
        if clts_feature_values.get(feature, {"domain": ""})["domain"] in clts_feature_hierarchy:
            primary_features.append(feature)
        else:
            secondary_features.append(feature)

    return __order_features(primary_features), secondary_features


def __apply_feature(feature, base_vec):
    bin_feature_vec = clts_feature_values.get(feature, {"features": {}})["features"]
    for k, v in bin_feature_vec.items():
        if v in [1, -1]:
            base_vec[k] = v

    return base_vec


def __apply_positive_features(feature, base_vec):
    bin_feature_vec = clts_feature_values.get(feature, {"features": {}})["features"]
    for k, v in bin_feature_vec.items():
        if v == 1:
            base_vec[k] = v

    return base_vec


def __apply_joint_feature_definitions(sound, base_vec):
    for features, bin_feature_vec in joint_feature_definitions.items():
        if set(features).issubset(sound.featureset):
            for k, v in bin_feature_vec.items():
                if v in [1, -1]:
                    base_vec[k] = v

    return base_vec
