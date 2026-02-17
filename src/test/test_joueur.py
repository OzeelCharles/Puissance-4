import pytest as pt
from interface.Grille import Grille
from players.Joueur import Joueur
import random


@pt.fixture
def random_player_T(grille_jeu):
    return Joueur(grille_jeu, True)


@pt.fixture
def random_player_F():
    grille_jeu = Grille()
    return Joueur(grille_jeu, False)


def test_play_T(random_player_T):
    random.seed(42)
    res = random_player_T.play()
    random_player_T.Grille == res


def test_play_F(random_player_F):
    random.seed(42)
    res = random_player_F.play()
    random_player_F.Grille == res


def test_play_after_win_T(random_player_T):
    for _ in range(4):
        random_player_T.Grille.add_token(0, False)
    test = random_player_T.Grille.copy()
    assert random_player_T.play().Grille == test.Grille
