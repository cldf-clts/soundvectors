import pytest
from clts2vec.parse import Vector


@pytest.fixture
def vector():
    v = Vector(["cons", "syl", "cont"])
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
