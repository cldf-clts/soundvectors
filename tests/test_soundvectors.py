import types
import pathlib

import pytest
from soundvectors import SoundVectors, is_valid_sound, FeatureBundle
from linse.annotate import clts


@pytest.fixture
def sv():
    return SoundVectors(ts=clts)


@pytest.mark.parametrize(
    'sound,expected',
    [
        ('voiceless alveolar stop consonant', True),
        ('some vowel', True),
        ('???', False),
        (None, False),
        (1, False),
    ]
)
def test_is_valid_sound(sound, expected):
    assert is_valid_sound(sound) is expected


def test_call_invalid(sv):
    with pytest.warns(UserWarning):
        sv([None])


def test_clts_compat(sv):
    from pyclts import CLTS

    clts = CLTS(pathlib.Path(__file__).parent / 'fixtures' / 'clts')
    assert sv.clts_compatibility(clts)
    assert SoundVectors(ts=clts.bipa).get_vec('a')


def test_parse_simple(sv):
    vec = (1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0)
    vec_dict = {'cons': 1, 'syl': -1, 'son': -1, 'cont': -1, 'delrel': -1, 'lat': -1, 'nas': -1, 'voi': -1, 'sg': -1,
                'cg': -1, 'pharyngeal': -1, 'laryngeal': -1, 'cor': 1, 'dorsal': -1, 'lab': -1, 'hi': -1, 'lo': -1,
                'back': -1, 'front': 1, 'tense': 0, 'round': -1, 'velaric': -1, 'long': -1, 'ant': 1, 'distr': -1,
                'strid': 0, 'hitone': 0, 'hireg': 0, 'loreg': 0, 'rising': 0, 'falling': 0, 'contour': 0, 'backshift': 0,
                'frontshift': 0, 'opening': 0, 'closing': 0, 'centering': 0, 'longdistance': 0, 'secondrounded': 0}
    assert sv.get_vec("t") == vec
    assert sv.get_vec(clts(["t"])[0]) == vec

    assert sv.get_vec("t", vectorize=False) == vec_dict


def test_parse_diacritics(sv):
    res = sv["long devoiced voiced labio-dental fricative consonant"]
    assert res.voi == -1
    assert res.long == 1


def test_parse_diphthong(sv):
    vec_dict = sv.get_vec("from unrounded open front to unrounded close front diphthong", vectorize=False)
    assert vec_dict["lo"] == 1
    assert vec_dict["hi"] == -1
    assert vec_dict["closing"] == 1
    assert vec_dict["opening"] == -1
    assert vec_dict["longdistance"] == 1
    assert vec_dict["secondrounded"] == -1


def test_parse_diphthong_long(sv):
    assert sv.get_vec("aiː") == sv.get_vec("aːi") == sv.get_vec("aːiː")
    vec_dict = sv.get_vec("aiː", vectorize=False)
    assert vec_dict["long"] == 1


def test_parse_diphthong_nas(sv):
    sound1 = "from nasalized unrounded open front to unrounded close front diphthong"
    sound2 = "from unrounded open front to nasalized unrounded close front diphthong"
    sound3 = "from nasalized unrounded open front to nasalized unrounded close front diphthong"

    assert sv.get_vec(sound1) == sv.get_vec(sound2) == sv.get_vec(sound3)
    vec_dict = sv.get_vec(sound2, vectorize=False)
    assert vec_dict["nas"] == 1


def test_parse_cluster(sv):
    # [kp] should have features for both places of articulation (labial & velar), but not for
    # other ones (e.g. coronal)
    vec_dict = sv.get_vec("kp", vectorize=False)
    assert vec_dict["hi"] == 1
    assert vec_dict["lab"] == 1
    assert vec_dict["cor"] == -1

    # in case of "conflicting" features (like voicing in [kg]), the positive one is assigned
    vec_dict = sv.get_vec("kg", vectorize=False)
    assert vec_dict["voi"] == 1


@pytest.mark.parametrize(
    'sound,as_set',
    [
        ('5', {"+hitone", "+hireg", "-loreg", "-rising", "-falling", "-contour"}),
        ('51', {"+hitone", "+hireg", "-loreg", "-rising", "+falling", "-contour"}),
        ('513', {"+hitone", "+hireg", "-loreg", "-rising", "+falling", "+contour"}),
    ]
)
def test_parse_tone(sound, as_set, sv):
    # for tones, ONLY the six tonal features should have actual (non-zero) values:
    # ["hitone", "hireg", "loreg", "rising", "falling", "contour"]
    assert sv[sound].as_set() == as_set


def test_parse_non_sound(sv):
    with pytest.warns(UserWarning):
        with pytest.raises(ValueError):
            sv.get_vec("AAA")

    with pytest.warns(UserWarning):
        with pytest.raises(ValueError):
            sv.get_vec(clts(["AAA"])[0])

    with pytest.raises(ValueError):
        sv.get_vec("")

    with pytest.warns(UserWarning):
        with pytest.raises(ValueError):
            sv.get_vec(clts([""]))

    with pytest.raises(ValueError):
        sv.get_vec(None)


def test_call(sv):
    res = sv(["a", "l"], vectorize=False)
    assert len(res) == 2

    a_vec, l_vec = res
    assert a_vec["cons"] == -1
    assert a_vec["syl"] == 1
    assert l_vec["cons"] == 1
    assert l_vec["syl"] == -1


def test_validate():
    class MockCLTS:
        def __call__(self, item):
            return [types.SimpleNamespace(name=clts([i])[0]) for i in item]

    mcts = MockCLTS()
    c2v = SoundVectors(ts=mcts)
    assert c2v.validate("t") == mcts(["t"])[0].name
    assert c2v.validate(mcts(["t"])[0]) == mcts(["t"])[0].name


@pytest.fixture
def vector():
    return FeatureBundle(cons=1, syl=-1)


def test_vector_as_set(vector):
    assert frozenset({"+cons", "-syl"}) == vector.as_set()


@pytest.mark.parametrize('substr', ['+cons', '-syl', '0_cont'])
def test_vec_as_str(substr, vector):
    assert substr in str(vector)


def test_rare_clts_sounds(bipa):
    sv = SoundVectors()
    assert sv[bipa['äu̽'].name]


def test_clts_sounds(clts_sound_and_vector, bipa):
    sound, expected = clts_sound_and_vector
    sv = SoundVectors()
    assert sv.get_vec(bipa[sound]) == expected
