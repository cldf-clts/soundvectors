from clts2vec.utils import vec_to_str, vec_to_feature_set


def test_vec_to_feature_set():
    assert frozenset({"+cons", "-syl"}) == vec_to_feature_set([1, -1]) == vec_to_feature_set([1, -1, 0])


def test_vec_to_str():
    exp = ("+cons,-syl,-son,-cont,-delrel,-lat,-nas,-voi,-sg,-cg,-pharyngeal,-laryngeal,+cor,-dorsal,-lab,-hi,-lo,"
           "-back,+front,0_tense,-round,-velaric,-long,+ant,-distr,0_strid,0_hitone,0_hireg,0_loreg,0_rising,"
           "0_falling,0_contour,0_backshift,0_frontshift,0_opening,0_closing,0_centering,0_longdistance,"
           "0_secondrounded")
    vec = (1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 0, -1, -1, -1, 1, -1, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0)

    assert vec_to_str(vec) == exp
