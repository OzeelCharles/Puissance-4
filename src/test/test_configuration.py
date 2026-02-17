from interface.Configuration import Configuration
import pytest as pt
from itertools import product


@pt.fixture
def config():
    return Configuration()


def test_next_player_F(config):
    config.add_token(0, True)
    assert config.who_s_playing_after() is False


def test_next_player_T(config):
    config.add_token(0, False)
    assert config.who_s_playing_after() is True


def test_next_player_N(config):
    for _, colonne in product(range(6), range(7)):
        config.add_token(colonne, True)
    assert config.who_s_playing_after() is None


def test_config_suivante(config):
    res = list(config.config_suivante())
    test_grille = Configuration()
    test = [test_grille.copy().add_token(i, False) for i in range(7)]
    assert res == test

    for _ in range(3):
        config.add_token(0, False)
        config.add_token(4, True)
    res = list(config.est_gagnante())
    test = [False, None, None, None, True, None, None]
    assert res == test
