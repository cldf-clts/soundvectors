"""
Base script for handling CLTS vectorization.
"""
from clts2vec.features import (
    clts_feature_values, joint_feature_definitions,
    clts_feature_hierarchy, max_hierarchy_level, binary_features)
from collections import OrderedDict


def is_valid_sound(sound):
    """
    Check if sound corresponds to our expectations.

    @note: We expect a string à la "voiced bilabial stop consonant"
    """
    if isinstance(sound, str) and (sound.endswith(" consonant") or sound.endswith(" vowel") or
            sound.endswith(" tone") or sound.endswith(" diphthong") or
            sound.endswith(" cluster")):
        return True
    return False


class Vector(OrderedDict):

    def __init__(self, features):
        OrderedDict.__init__(OrderedDict())
        for f in features:
            self[f] = 0

    def __str__(self):
        return ",".join([
            {1: "+", -1: "-", 0: "0_"}[v] + k for k, v in self.items()])

    def as_vec(self):
        return tuple(self.values())

    def as_set(self):
        return frozenset({{1: "+", -1: "-"}[v] + k for k, v in self.items() if v})


class CLTS2Vec:
    """
    CLTS2Vec handles vectorization of sounds represented by features.

    Examples::
        >>> from clts2vec import CLTS2Vec
        >>> c2v = CLTS2Vec()
        >>> c2v
    """

    feature_values = clts_feature_values
    binary_features = binary_features
    joint_defs = joint_feature_definitions
    feature_hierarchy = clts_feature_hierarchy
    ts = None

    def __init__(
            self,
            ts=None,
            feature_values=None,
            feature_hierarchy=None,
            binary_features=None,
            joint_defs=None
    ):

        self.ts = ts
        self.feature_values = feature_values or self.feature_values
        self.joint_defs = joint_defs or self.joint_defs
        self.feature_hierarchy = feature_hierarchy or self.feature_hierarchy
        self.binary_features = binary_features or self.binary_features

    def __call__(self, sounds, vectorize=True):
        return [self.get_vec(sound, vectorize=vectorize) for sound in sounds]

    def validate(self, sound):
        """
        Try to retrieve the sound name from CLTS or `linse`.
        """
        if is_valid_sound(sound):
            return sound
        if sound and self.ts:
            sound = self.ts([sound])[0]
            if hasattr(sound, "name"):
                sound = sound.name
            if is_valid_sound(sound):
                return sound
        raise ValueError("Invalid sound encountered.")

    def get_vec(self, sound, vectorize=True):
        """
        Retrieve the vector for a given sound.

        @param sound: A sound represented by a feature string. If a
            transcription system has been supplied, it can also be a 
            sound in IPA notation.
        @param vectorize: Return a binary vector if set to True.
        @returns: vector (dictionary of feature values or tuple of values)
        
        Examples::
            
            >>> from clts2vec import CLTS2Vec
            >>> c2v = CLTS2Vec()
            >>> vec = c2v.get_vec("t", vectorize=False)
            >>> print(vec["cont"]
            - 1
        """
        sound = self.validate(sound)
        base_vec = Vector(self.binary_features)  # {f: 0 for f in self.binary_features}

        # check if sound is diphthong or complex
        complex_sound = False
        if sound.endswith(" diphthong"):
            self._apply_feature("diphthong", base_vec)
            sound_to_sound = sound[sound.index(" to ") + 4: -10] + " vowel"
            sound = sound[5: sound.index(" to ")] + " vowel"
            # set up feature pairs for diphthong trajectory
            diphthong_features = (["from_" + f for f in sound.split()[:-1]] +
                                  ["to_" + f for f in sound_to_sound.split()[:-1]])
            complex_sound = "diphthong"

        elif sound.endswith(" cluster"):
            sound_to_sound = sound[sound.index(" to ") + 4: -8] + " consonant"
            sound = sound[5: sound.index(" to ")] + " consonant"
            complex_sound = "cluster"

        features = [f for df in sound.split() for f in df.split("-and-")]

        primary_features, secondary_features = self._get_features(features)

        for feature in primary_features:
            self._apply_feature(feature, base_vec)

        # diphthongs take their core vowel features from their first vowel,
        # diphthong-specific features are then applied afterwards
        if complex_sound == "diphthong":
            # apply joint diphthong features
            self._apply_joint_feature_defs(diphthong_features, base_vec)
            # check for duration
            if "long" in sound_to_sound or "short" in sound_to_sound:
                duration = [f for f in sound_to_sound.split() if ("long" in f
                                                                  or "short" in f)][0]
                self._apply_positive_features(duration, base_vec)
            # assign [+nas] if second part of the diphthong is nasalized
            if "nasalized" in sound_to_sound:
                self._apply_positive_features("nasalized", base_vec)
        elif complex_sound == "cluster":
            from_vec = self.get_vec(sound, vectorize=False)
            to_vec = self.get_vec(sound_to_sound, vectorize=False)
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
        return base_vec.as_vec()

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

    def _apply_positive_features(self, feature, base_vec):
        bin_feature_vec = self.feature_values.get(
            feature, {"features": {}})["features"]
        for k, v in bin_feature_vec.items():
            if v == 1:
                base_vec[k] = v
