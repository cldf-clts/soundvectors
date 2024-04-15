"""
Base script for handling CLTS vectorization.
"""
from clts2vec.features import (
        clts_feature_values, joint_feature_definitions, 
        clts_feature_hierarchy, max_hierarchy_level, binary_features)


class CLTS2Vec:

    feature_values = clts_feature_values
    binary_features = binary_features
    joint_defs = joint_feature_definitions
    feature_hierarchy = clts_feature_hierarchy

    def __init__(self):

        pass

    def _get_features(self, featureset):
        
        primary_features, secondary_features = [], []
        for feature in featureset:
            if self.feature_values.get(
                    feature, {"domain": ""}
                    )["domain"] in self.feature_hierarchy:
                primary_features.append(feature)
            else:
                secondary_features.append(feature)
        primary_features = sorted(
                primary_features,
                key=lambda x: self.feature_hierarchy.get(
                    self.feature_values.get(
                        x, {"domain": ""})["domain"], 
                    max_hierarchy_level))

        return primary_features, secondary_features

    def _apply_feature(self, feature, base_vec):
        bin_feature_vec = self.feature_values.get(
                feature, {"features": {}})["features"]
        for k, v in bin_feature_vec.items():
            if v in [1, -1]:
                base_vec[k] = v

    def _apply_joint_feature_defs(self, sound_features, base_vec):
        for features, bin_feature_vec in self.joint_defs.items():
            if set(features).issubset(set(sound_features)):
                for k, v in bin_feature_vec.items():
                    if v in [1, -1]:
                        base_vec[k] = v

    def __apply_positive_features(self, feature, base_vec):
        bin_feature_vec = self.feature_values.get(
                feature, {"features": {}})["features"]
        for k, v in bin_feature_vec.items():
            if v == 1:
                base_vec[k] = v


    def __call__(self, sound):
        return self._parse(sound)

    def parse(self, sound, vectorize=True):
        
        base_vec = {f: 0 for f in self.binary_features}

        # check if sound is diphthong
        complex_sound = False
        
        if sound.endswith(" diphthong"):
            sound_to_sound = sound[sound.index(" to ") + 4: -10] + " vowel"
            sound = sound[5: sound.index(" to ")] + " vowel"
            complex_sound = "diphthong"

        elif sound.endswith(" cluster"):
            sound_to_sound = sound[sound.index(" to ") + 4: -8] + " consonant"
            sound = sound[5: sound.index(" to ")] + " consonant"
            complex_sound = "cluster"

        features = [f for df in sound.split() for f in df.split("-and-")][:-1]

        primary_features, secondary_features = self._get_features(features)

        for feature in primary_features:
            self._apply_feature(feature, base_vec)

        ## diphthongs take their core vowel features from their first vowel,
        ## diphthong-specific features are then applied afterwards
        if complex_sound == "diphthong":
            print(sound_to_sound)
            # assign [+long] if second part of the diphthong is long
            #if sound.to_sound.duration:
            #    base_vec = _apply_positive_features(sound.to_sound.duration, base_vec)
            # assign [+nas] if second part of the diphthong is nasalized
            if " nasalized " in sound_to_sound:
                self._apply_positive_features("nasalized", base_vec)
        elif complex_sound == "cluster":
            from_vec = self.parse(sound, vectorize=False)
            to_vec = self.parse(sound_to_sound, vectorize=False)
            for f in binary_features:
                if from_vec[f] == 1 or to_vec[f] == 1:
                    base_vec[f] = 1
                elif from_vec[f] == -1 or to_vec[f] == -1:
                    base_vec[f] = -1
                else:
                    base_vec[f] = 0

        self._apply_joint_feature_defs(features, base_vec)

        for feature in secondary_features:
            self._apply_feature(feature, base_vec)

        if not vectorize:
            return base_vec

        return tuple([base_vec[f] for f in binary_features])










def __apply_positive_features(feature, base_vec):
    bin_feature_vec = clts_feature_values.get(feature, {"features": {}})["features"]
    for k, v in bin_feature_vec.items():
        if v == 1:
            base_vec[k] = v

    return base_vec


