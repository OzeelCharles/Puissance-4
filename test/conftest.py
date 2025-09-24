import pytest
from Grille import Grille


@pytest.fixture
def sample_grille():
    return Grille()


@pytest.fixture
def sample_full_grille():
    res = Grille()
    for i in range(6):
        res.ajout_jeton(0, True)
    return res


@pytest.fixture
def sample_True_v():
    res = Grille()
    for i in range(4):
        res.ajout_jeton(0, True)
    return res


@pytest.fixture
def sample_False_v():
    res = Grille()
    for i in range(4):
        res.ajout_jeton(0, False)
    return res


@pytest.fixture
def sample_True_h():
    res = Grille()
    for i in range(4):
        res.ajout_jeton(i, True)
    return res


@pytest.fixture
def sample_False_h():
    res = Grille()
    for i in range(4):
        res.ajout_jeton(i, False)
    return res


@pytest.fixture
def sample_True_d_a():
    res = Grille()
    for i in range(3):
        res.ajout_jeton(i, False)
    for i in range(2):
        res.ajout_jeton(i, False)
    res.ajout_jeton(0, False)
    for i in range(4):
        res.ajout_jeton(i, True)
    return res


@pytest.fixture
def sample_False_d_a():
    res = Grille()
    for i in range(3):
        res.ajout_jeton(i, True)
    for i in range(2):
        res.ajout_jeton(i, True)
    res.ajout_jeton(0, True)
    for i in range(4):
        res.ajout_jeton(i, False)
    return res


@pytest.fixture
def sample_True_d_d():
    res = Grille()
    for i in range(3):
        res.ajout_jeton(2 + i, False)
    for i in range(2):
        res.ajout_jeton(3 + i, False)
    res.ajout_jeton(4, False)
    for i in range(4):
        res.ajout_jeton(1 + i, True)
    return res


@pytest.fixture
def sample_False_d_d():
    res = Grille()
    for i in range(3):
        res.ajout_jeton(2 + i, True)
    for i in range(2):
        res.ajout_jeton(3 + i, True)
    res.ajout_jeton(4, True)
    for i in range(4):
        res.ajout_jeton(1 + i, False)
    return res


@pytest.fixture
def neutral():
    res = Grille()
    res.ajout_jeton(0, True)
    res.ajout_jeton(2, False)
    res.ajout_jeton(1, False)
    res.ajout_jeton(4, True)
    res.ajout_jeton(4, True)
    return res


@pytest.fixture
def equality():
    res = Grille()
    for _ in range(3):
        res.ajout_jeton(0, True)
        res.ajout_jeton(0, False)
        res.ajout_jeton(1, False)
        res.ajout_jeton(1, True)

    for _ in range(3):
        res.ajout_jeton(2, False)
        res.ajout_jeton(2, True)
        res.ajout_jeton(3, True)
        res.ajout_jeton(3, False)

    # Colonnes 4 et 5
    for _ in range(3):
        res.ajout_jeton(4, True)
        res.ajout_jeton(4, False)
        res.ajout_jeton(5, False)
        res.ajout_jeton(5, True)

    # Colonne 6 (dernière colonne)
    for _ in range(3):
        res.ajout_jeton(6, False)
        res.ajout_jeton(6, True)

    return res


@pytest.fixture
def joueur_grille():
    return Grille()
