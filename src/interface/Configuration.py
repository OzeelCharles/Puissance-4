from interface.Grille import Grille
from itertools import product


class Configuration(Grille):
    def who_s_playing_after(self):
        if self.Check() is None:
            res_T = sum(
                self.Grille[ligne][colonne] is True
                for ligne, colonne in product(range(6), range(7)))
            res_F = sum(
                self.Grille[ligne][colonne] is False
                for ligne, colonne in product(range(6), range(7)))
            res = res_T - res_F
            return res == -1
        return None

    def config_suivante(self, token=None):
        token = self.who_s_playing_after() if token is None else token
        if token is not None:
            for i in range(7):
                res = self.copy()
                res.add_token(i, token)
                yield res
                i += 1
        return None

    def est_gagnante(self, token=None, n_token=None):
        if token not in {None, True} and n_token not in {None, True}:
            raise ValueError
        if token == n_token and token is not None:
            raise ValueError
        if token is None and n_token is None:
            token = self.who_s_playing_after()
            if token is not None:
                config_token = self.config_suivante(token)
                config_not_token = self.config_suivante(not token)
                for _ in range(7):
                    check_t = next(config_token).Check()
                    check_nt = next(config_not_token).Check()
                    yield check_t if check_nt is None else check_nt
            return None
        if token is not None:
            token = self.who_s_playing_after()
            if token is not None:
                config_token = self.config_suivante(token)
                for _ in range(7):
                    yield next(config_token).Check()
            return None
        token = not self.who_s_playing_after()
        if token is not None:
            config_not_token = self.config_suivante(token)
            for _ in range(7):
                yield next(config_not_token).Check()

    def est_gagnante2(self):
        """
        Doit renvoyer un générateur qui dit si
        le coup suivant qu'on va jouer est
        avantageux ou non pour l'adversaire
        """
        token = self.who_s_playing_after()
        if token is not None:
            config_jouable = self.config_suivante(token)
            for _ in range(7):
                yield any(
                    res is not token for res in next(
                        config_jouable).est_gagnante(True, None))
        return None

    def config_suivante2(self, token=None):
        token = self.who_s_playing_after() if token is None else token
        if token is not None:
            flayer = self.config_suivante()
            for _ in range(7):
                yield next(flayer).config_suivante()
        return None


"""""
    def apres(self):
        "un niveau au dessus"
        config = self.configuration_suivante()
        for _ in range(7):
            yield next(config).configuration_suivante()
    # Créer générateur des configurations suivantes des configs suivantes #
    # (donc 7 listes de 7 config possible) #

    def apres2(self):
        config = self.apres()
        i = 0
        while i < 7:
            j = 0
            config_2 = next(config)
            while j < 7:
                yield list(next(config_2).est_gagnante())
                j += 1
            i += 1

        # Créer un générateur d'au plus 49 liste de config gagnante ou non#

    def config_possiblement_gagnante(self):
        jeton = self.who_s_playing_after()
        config = self.apres2()
        i = 0
        while i < 49:
            if jeton in next(config):
                return True
            i += 1
        return False

    def config_virtuellement_gagnante(self, a=0):
        jeton = self.who_s_playing_after()
        if self.config_possiblement_gagnante():
            return True
        B = self.copy()
        B.ajout_jeton(a, jeton)
        B.ajout_jeton(a, jeton).ajout_jeton(a, jeton)

        # PB: je dois faire jouer True et False dans les 49 positions
        # possibles pour leurs applqieur ensuite la boucle #

    def est_gagnante2(self):

        à partir du coup qu'on peut faire,
        renvoie si le coup au dessus est favorable ou non à l'adversaire

        config_token = self.config_suivante()
        for _ in range(7):
            check = next(config_token).est_gagnante()
"""
