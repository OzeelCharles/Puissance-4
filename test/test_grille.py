import pytest as pt


def test_init(sample_grille):
    assert sample_grille.Grille == tuple(
        tuple(None for i in range(7)) for j in range(6)
    )


def test_repr(sample_grille):
    assert (
        repr(sample_grille)
        == """(None, None, None, None, None, None, None)
(None, None, None, None, None, None, None)
(None, None, None, None, None, None, None)
(None, None, None, None, None, None, None)
(None, None, None, None, None, None, None)
(None, None, None, None, None, None, None)
"""
    )


@pt.mark.parametrize(
    "colonne, jeton, res, message",
    [
        (5, None, TypeError, "Couleur doit être un booléen, pas NoneType"),
        (-1, True, ValueError, "-1 n'est pas compris entre 0 et 6."),
        (7, False, ValueError, "7 n'est pas compris entre 0 et 6."),
        (2, "", TypeError, "Couleur doit être un booléen, pas str"),
        (
            2,
            False,
            (
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, None, None),
                (None, None, False, None, None, None, None),
            ),
            None,
        ),
        (
            5,
            True,
            (
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, None, None),
                (None, None, None, None, None, True, None),
            ),
            None,
        ),
        (
            0,
            True,
            (
                (True, None, None, None, None, None, None),
                (True, None, None, None, None, None, None),
                (True, None, None, None, None, None, None),
                (True, None, None, None, None, None, None),
                (True, None, None, None, None, None, None),
                (True, None, None, None, None, None, None),
            ),
            None,
        ),
    ],
)
def test_ajout_jeton(sample_grille, sample_full_grille, colonne, jeton, res, message):
    if not message:
        if colonne != 0:
            sample_grille.ajout_jeton(colonne, jeton)
            assert sample_grille.Grille == res
        else:
            sample_full_grille.ajout_jeton(colonne, jeton)
            assert sample_full_grille.Grille == res

    else:
        with pt.raises(res) as exc_info:
            sample_grille.ajout_jeton(colonne, jeton)
        assert message in str(exc_info.value)


def test_Check_true(
    sample_True_v, sample_True_h, sample_True_d_a, sample_True_d_d, neutral
):
    assert sample_True_v.check_True() == True
    assert sample_True_h.check_True() == True
    assert sample_True_d_a.check_True() == True
    assert sample_True_d_d.check_True() == True
    assert neutral.check_False() is None


def test_Check_False(
    sample_False_v, sample_False_h, sample_False_d_a, sample_False_d_d, neutral
):
    assert sample_False_v.check_False() == False
    assert sample_False_h.check_False() == False
    assert sample_False_d_a.check_False() == False
    assert sample_False_d_d.check_False() == False
    assert neutral.check_False() is None


def test_Check(
    sample_True_v,
    sample_True_h,
    sample_True_d_a,
    sample_True_d_d,
    neutral,
    sample_False_v,
    sample_False_h,
    sample_False_d_a,
    sample_False_d_d,
    equality,
):
    assert sample_True_v.Check() == True
    assert sample_True_h.Check() == True
    assert sample_True_d_a.Check() == True
    assert sample_True_d_d.Check() == True
    assert neutral.Check() is None
    assert sample_False_v.Check() == False
    assert sample_False_h.Check() == False
    assert sample_False_d_a.Check() == False
    assert sample_False_d_d.Check() == False
    assert equality.Check() == "tableau plein, impossible de finir"
