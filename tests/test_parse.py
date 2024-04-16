import pytest
from pyclts import CLTS
from clts2vec.parse import CLTS2Vec, is_valid_sound


@pytest.fixture
def bipa():
    return CLTS().bipa


@pytest.fixture
def c2v(bipa):
    return CLTS2Vec(ts=bipa)


def test_is_valid_sound():
    assert is_valid_sound("voiceless alveolar stop consonant")
    assert is_valid_sound("some vowel")
    assert not is_valid_sound("???")
    assert not is_valid_sound(None)
    assert not is_valid_sound(1)


def test_parse_simple(bipa, c2v):
    vec = (1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0)
    vec_dict = {'cons': 1, 'syl': -1, 'son': -1, 'cont': -1, 'delrel': -1, 'lat': -1, 'nas': -1, 'voi': -1, 'sg': -1,
                'cg': -1, 'pharyngeal': -1, 'laryngeal': -1, 'cor': 1, 'dorsal': -1, 'lab': -1, 'hi': -1, 'lo': -1,
                'back': -1, 'front': 1, 'tense': 0, 'round': -1, 'velaric': -1, 'long': -1, 'ant': 1, 'distr': -1,
                'strid': 0, 'hitone': 0, 'hireg': 0, 'loreg': 0, 'rising': 0, 'falling': 0, 'contour': 0, 'backshift': 0,
                'frontshift': 0, 'opening': 0, 'closing': 0, 'centering': 0, 'longdistance': 0, 'secondrounded': 0}
    assert c2v.get_vec("t") == c2v.get_vec(bipa["t"]) == vec
    assert c2v.get_vec("t", vectorize=False) == vec_dict


def test_parse_diacritics(c2v):
    vec_dict = c2v.get_vec("v̥ː", vectorize=False)
    assert vec_dict["voi"] == -1
    assert vec_dict["long"] == 1


def test_parse_diphthong(c2v):
    vec_dict = c2v.get_vec("ai", vectorize=False)
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
    assert c2v.get_vec("ãi") == c2v.get_vec("aĩ") == c2v.get_vec("ãĩ")
    vec_dict = c2v.get_vec("aĩ", vectorize=False)
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


def test_parse_non_sound(bipa, c2v):
    with pytest.raises(ValueError):
        c2v.get_vec("AAA")

    with pytest.raises(ValueError):
        c2v.get_vec(bipa["AAA"])

    with pytest.raises(ValueError):
        c2v.get_vec("")

    with pytest.raises(ValueError):
        c2v.get_vec(bipa[""])

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

