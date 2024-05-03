import pytest

from soundvectors import SoundVectors


@pytest.fixture
def sv():
    return SoundVectors()


def test_cluster_kp(bipa, sv):
    """
    The resulting feature vector for [kp] therefore contains all positive features that are
    attributed to either [k] or [p].
    """
    def positive_features(sound):
        return set(sv[bipa[sound].name].as_dict(valid_values={1}).keys())

    assert positive_features('p').issubset(positive_features('kp'))
    assert positive_features('k').issubset(positive_features('kp'))


def test_glottal_stop(bipa, sv):
    """
    For example, the glottal stop [P] has the binary feature [+cg] (‘constricted glottis’).
    """
    assert sv[bipa['ʔ'].name].cg == 1


def test_devoiced_voiced(bipa, sv):
    """
    To exemplify this, consider the ‘devoiced voiced labio-dental fricative’ [v ̊]: The descriptor
    ‘voiced’ maps to [+voice], whereas ‘devoiced’ naturally corresponds to [-voice]. However,
    since diacritics modify the base sound, they should take precedence over it, and the correct
    feature that should be assigned is [-voice].
    """
    assert sv[bipa["v̥"].name].voi == -1


def test_diphthong_ai(bipa, sv):
    """
    For example, [aI] gets its monophthong vowel features from the feature definitions for [a].
    The additional diphthong features, that indicate the trajectory of the diphthong, are assigned
    based on joint feature definitions: The combination of the CLTS features (‘from_open’,
    ‘to_near-close’) maps (among others) to the binary feature [+closing].
    """
    assert sv[bipa["aɪ"].name].closing == 1
