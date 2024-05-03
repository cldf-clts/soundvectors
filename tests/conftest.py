import random
import pathlib

import pytest
from pyclts import CLTS

FIXTURES = pathlib.Path(__file__).parent / 'fixtures'


def pytest_addoption(parser):
    parser.addoption("--all", action="store_true", help="run all CLTS sound checks")


@pytest.fixture
def bipa():
    return CLTS(FIXTURES / 'clts').bipa


def pytest_generate_tests(metafunc):
    def iter_sounds():
        for line in FIXTURES.joinpath('sounds.tsv').read_text(encoding='utf-8').split('\n'):
            if line:
                sound, _, vec = line.partition('\t')
                yield sound, eval(vec)

    sounds = list(iter_sounds())
    if not metafunc.config.getoption("all"):
        sounds = random.sample(sounds, 100)

    if "clts_sound_and_vector" in metafunc.fixturenames:
        metafunc.parametrize("clts_sound_and_vector", sounds)
