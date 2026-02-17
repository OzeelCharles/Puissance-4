import pytest as pt
from unittest.mock import patch
from interface.Grille import Grille
from players.JoueurHumain import JoueurHumain


@pt.fixture
def humanplayer():
    grille = Grille()
    return JoueurHumain(grille, True)


def test_play_input(humanplayer):
    test = humanplayer.Grille.copy()
    test.add_token(3, True)
    with patch("builtins.input", return_value="3"):
        res = humanplayer.play()
        assert res.Grille == test.Grille
