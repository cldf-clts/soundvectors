import pytest
from pyclts import CLTS
from clts2vec.parse import parse


@pytest.fixture
def bipa():
    return CLTS().bipa


def test_parse_simple(bipa):
    vec = (1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0)
    vec_dict = {'cons': 1, 'syl': -1, 'son': -1, 'cont': -1, 'delrel': -1, 'lat': -1, 'nas': -1, 'voi': -1, 'sg': -1,
                'cg': -1, 'pharyngeal': -1, 'laryngeal': -1, 'cor': 1, 'dorsal': -1, 'lab': -1, 'hi': -1, 'lo': -1,
                'back': -1, 'front': 1, 'tense': 0, 'round': -1, 'velaric': -1, 'long': -1, 'ant': 1, 'distr': -1,
                'strid': 0, 'hitone': 0, 'hireg': 0, 'loreg': 0, 'rising': 0, 'falling': 0, 'contour': 0, 'backshift': 0,
                'frontshift': 0, 'opening': 0, 'closing': 0, 'centering': 0, 'longdistance': 0, 'secondrounded': 0}
    assert parse("t") == parse(bipa["t"]) == vec
    assert parse("t", vectorize=False) == vec_dict


def test_parse_diacritics():
    vec_dict = parse("v̥ː", vectorize=False)
    assert vec_dict["voi"] == -1
    assert vec_dict["long"] == 1


def test_parse_diphthong():
    vec_dict = parse("ai", vectorize=False)
    assert vec_dict["lo"] == 1
    assert vec_dict["hi"] == -1
    assert vec_dict["closing"] == 1
    assert vec_dict["opening"] == -1
    assert vec_dict["longdistance"] == 1
    assert vec_dict["secondrounded"] == -1


def test_parse_diphthong_long():
    assert parse("aiː") == parse("aːi") == parse("aːiː")
    vec_dict = parse("aiː", vectorize=False)
    assert vec_dict["long"] == 1


def test_parse_diphthong_nas():
    assert parse("ãi") == parse("aĩ") == parse("ãĩ")
    vec_dict = parse("aĩ", vectorize=False)
    assert vec_dict["nas"] == 1


def test_parse_cluster():
    # [kp] should have features for both places of articulation (labial & velar), but not for other ones (e.g. coronal)
    vec_dict = parse("kp", vectorize=False)
    assert vec_dict["hi"] == 1
    assert vec_dict["lab"] == 1
    assert vec_dict["cor"] == -1

    # in case of "conflicting" features (like voicing in [kg]), the positive one is assigned
    vec_dict = parse("kg", vectorize=False)
    assert vec_dict["voi"] == 1
