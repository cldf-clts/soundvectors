import pytest
from soundvectors import SoundVectors, is_valid_sound, FeatureBundle
from linse.annotate import clts
from collections import namedtuple


class MockCLTS:
    def __init__(self):
        pass

    def __call__(self, item):
        sound = namedtuple("sound", "name")
        out = []
        for item in item:
            out += [sound(clts([item])[0])]
        return out


@pytest.fixture
def c2v():
    return SoundVectors(ts=clts)


def test_is_valid_sound():
    assert is_valid_sound("voiceless alveolar stop consonant")
    assert is_valid_sound("some vowel")
    assert not is_valid_sound("???")
    assert not is_valid_sound(None)
    assert not is_valid_sound(1)


def test_parse_simple(c2v):
    vec = (1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0)
    vec_dict = {'cons': 1, 'syl': -1, 'son': -1, 'cont': -1, 'delrel': -1, 'lat': -1, 'nas': -1, 'voi': -1, 'sg': -1,
                'cg': -1, 'pharyngeal': -1, 'laryngeal': -1, 'cor': 1, 'dorsal': -1, 'lab': -1, 'hi': -1, 'lo': -1,
                'back': -1, 'front': 1, 'tense': 0, 'round': -1, 'velaric': -1, 'long': -1, 'ant': 1, 'distr': -1,
                'strid': 0, 'hitone': 0, 'hireg': 0, 'loreg': 0, 'rising': 0, 'falling': 0, 'contour': 0, 'backshift': 0,
                'frontshift': 0, 'opening': 0, 'closing': 0, 'centering': 0, 'longdistance': 0, 'secondrounded': 0}
    assert c2v.get_vec("t") == vec
    assert c2v.get_vec(clts(["t"])[0]) == vec

    assert c2v.get_vec("t", vectorize=False) == vec_dict


def test_parse_diacritics(c2v):
    vec_dict = c2v.get_vec("long devoiced voiced labio-dental fricative consonant", vectorize=False)
    assert vec_dict["voi"] == -1
    assert vec_dict["long"] == 1


def test_parse_diphthong(c2v):
    vec_dict = c2v.get_vec("from unrounded open front to unrounded close front diphthong", vectorize=False)
    assert vec_dict["lo"] == 1
    assert vec_dict["hi"] == -1
    assert vec_dict["closing"] == 1
    assert vec_dict["opening"] == -1
    assert vec_dict["longdistance"] == 1
    assert vec_dict["secondrounded"] == -1


def test_parse_diphthong_long(c2v):
    assert c2v.get_vec("aiː") == c2v.get_vec("aːi") == c2v.get_vec("aːiː")
    vec_dict = c2v.get_vec("aiː", vectorize=False)
    assert vec_dict["long"] == 1


def test_parse_diphthong_nas(c2v):
    sound1 = "from nasalized unrounded open front to unrounded close front diphthong"
    sound2 = "from unrounded open front to nasalized unrounded close front diphthong"
    sound3 = "from nasalized unrounded open front to nasalized unrounded close front diphthong"

    assert c2v.get_vec(sound1) == c2v.get_vec(sound2) == c2v.get_vec(sound3)
    vec_dict = c2v.get_vec(sound2, vectorize=False)
    assert vec_dict["nas"] == 1


def test_parse_cluster(c2v):
    # [kp] should have features for both places of articulation (labial & velar), but not for other ones (e.g. coronal)
    vec_dict = c2v.get_vec("kp", vectorize=False)
    assert vec_dict["hi"] == 1
    assert vec_dict["lab"] == 1
    assert vec_dict["cor"] == -1

    # in case of "conflicting" features (like voicing in [kg]), the positive one is assigned
    vec_dict = c2v.get_vec("kg", vectorize=False)
    assert vec_dict["voi"] == 1


def test_parse_tone(c2v):
    # for tones, ONLY the six tonal features should have actual (non-zero) values:
    # ["hitone", "hireg", "loreg", "rising", "falling", "contour"]
    vec_set = c2v.get_vec("5", vectorize=False).as_set()
    assert vec_set == frozenset({"+hitone", "+hireg", "-loreg", "-rising", "-falling", "-contour"})

    vec_set = c2v.get_vec("51", vectorize=False).as_set()
    assert vec_set == frozenset({"+hitone", "+hireg", "-loreg", "-rising", "+falling", "-contour"})

    vec_set = c2v.get_vec("513", vectorize=False).as_set()
    assert vec_set == frozenset({"+hitone", "+hireg", "-loreg", "-rising", "+falling", "+contour"})


def test_parse_non_sound(c2v):
    with pytest.raises(ValueError):
        c2v.get_vec("AAA")

    with pytest.raises(ValueError):
        c2v.get_vec(clts(["AAA"])[0])

    with pytest.raises(ValueError):
        c2v.get_vec("")

    with pytest.raises(ValueError):
        c2v.get_vec(clts([""]))

    with pytest.raises(ValueError):
        c2v.get_vec(None)


def test_call(c2v):
    res = c2v(["a", "l"], vectorize=False)
    assert len(res) == 2

    a_vec, l_vec = res
    assert a_vec["cons"] == -1
    assert a_vec["syl"] == 1
    assert l_vec["cons"] == 1
    assert l_vec["syl"] == -1


def test_validate():
    
    mcts = MockCLTS()
    c2v = SoundVectors(ts=mcts)
    assert c2v.validate("t") == mcts(["t"])[0].name


@pytest.fixture
def vector():
    v = FeatureBundle(["cons", "syl", "cont"])
    v["cons"] = 1
    v["syl"] = -1
    v["cont"] = 0

    return v


def test_vector_as_set(vector):
    assert frozenset({"+cons", "-syl"}) == vector.as_set()


def test_vec_as_str(vector):
    assert "+cons,-syl,0_cont" == str(vector)


def test_vec_as_vec(vector):
    assert (1, -1, 0) == vector.as_vec()
