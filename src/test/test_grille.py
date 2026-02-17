import pytest as pt
from interface.Grille import Grille


@pt.fixture
def sample_grille():
    return Grille()


@pt.fixture
def grille_comp():
    return Grille()


def test_init(sample_grille):
    assert sample_grille.Grille == [[None for _ in range(7)] for _ in range(6)]


def test_repr(sample_grille):
    assert (
        repr(sample_grille)
        == """[None, None, None, None, None, None, None]
[None, None, None, None, None, None, None]
[None, None, None, None, None, None, None]
[None, None, None, None, None, None, None]
[None, None, None, None, None, None, None]
[None, None, None, None, None, None, None]
""")


def test_eq(sample_grille, grille_comp):
    assert sample_grille == grille_comp
    sample_grille.add_token(0, True)
    assert sample_grille != grille_comp
    grille_comp.add_token(0, True)
    assert sample_grille == grille_comp


def test_copy(sample_grille):
    res = sample_grille.copy()
    assert id(res.Grille) != id(sample_grille.Grille)
    sample_grille.add_token(0, True)
    assert res.Grille != sample_grille.Grille


def test_check_True_no_winner(sample_grille):
    assert sample_grille.check_True() is None


def test_check_False_no_winner(sample_grille):
    assert sample_grille.check_False() is None


def test_check_True_winner_row(sample_grille):
    for col in range(4):
        sample_grille.add_token(col, True)
    assert sample_grille.check_True() is True


def test_check_False_winner_row(sample_grille):
    for col in range(4):
        sample_grille.add_token(col, False)
    assert sample_grille.check_False() is False


def test_check_False_winner_column(sample_grille):
    for _ in range(4):
        sample_grille.add_token(0, False)
    assert sample_grille.check_False() is False


def test_check_True_winner_diagonal(sample_grille):
    sample_grille.add_token(0, True)  # Row 5, Col 0
    sample_grille.add_token(1, False)
    sample_grille.add_token(1, True)  # Row 4, Col 1
    sample_grille.add_token(2, False)
    sample_grille.add_token(2, False)
    sample_grille.add_token(2, True)  # Row 3, Col 2
    sample_grille.add_token(3, False)
    sample_grille.add_token(3, False)
    sample_grille.add_token(3, False)
    sample_grille.add_token(3, True)  # Row 2, Col 3
    assert sample_grille.check_True() is True


def test_check_False_winner_diagonal(sample_grille):
    sample_grille.add_token(0, False)  # Row 5, Col 0
    sample_grille.add_token(1, True)
    sample_grille.add_token(1, False)  # Row 4, Col 1
    sample_grille.add_token(2, True)
    sample_grille.add_token(2, True)
    sample_grille.add_token(2, False)  # Row 3, Col 2
    sample_grille.add_token(3, True)
    sample_grille.add_token(3, True)
    sample_grille.add_token(3, True)
    sample_grille.add_token(3, False)  # Row 2, Col 3
    assert sample_grille.check_False() is False


def test_check_True_win(sample_grille):
    sample_grille.add_token(0, True)  # Row 5, Col 0
    sample_grille.add_token(1, False)
    sample_grille.add_token(1, True)  # Row 4, Col 1
    sample_grille.add_token(2, False)
    sample_grille.add_token(2, False)
    sample_grille.add_token(2, True)  # Row 3, Col 2
    sample_grille.add_token(3, False)
    sample_grille.add_token(3, False)
    sample_grille.add_token(3, False)
    sample_grille.add_token(3, True)  # Row 2, Col 3
    assert sample_grille.Check() is True


def test_check_False_win(sample_grille):
    sample_grille.add_token(0, False)  # Row 5, Col 0
    sample_grille.add_token(1, True)
    sample_grille.add_token(1, False)  # Row 4, Col 1
    sample_grille.add_token(2, True)
    sample_grille.add_token(2, True)
    sample_grille.add_token(2, False)  # Row 3, Col 2
    sample_grille.add_token(3, True)
    sample_grille.add_token(3, True)
    sample_grille.add_token(3, True)
    sample_grille.add_token(3, False)  # Row 2, Col 3
    assert sample_grille.Check() is False


def test_check_no_winners(sample_grille):
    assert sample_grille.Check() is None


def test_add_token(sample_grille):
    sample_grille.add_token(3, True)
    assert sample_grille.Grille[5][3] is True
    sample_grille.add_token(3, False)
    assert sample_grille.Grille[4][3] is False


def test_add_token_full_column(sample_grille):
    for _ in range(3):
        sample_grille.add_token(0, True)
        sample_grille.add_token(0, False)
    res = sample_grille.add_token(0, True)
    comp = Grille()
    comp.Grille = [[False, None, None, None, None, None, None],
                   [True, None, None, None, None, None, None],
                   [False, None, None, None, None, None, None],
                   [True, None, None, None, None, None, None],
                   [False, None, None, None, None, None, None],
                   [True, None, None, None, None, None, None]]
    assert res == comp
