from players.Joueur import Joueur


class JoueurNiveauUn(Joueur):
    def play(self):
        """
        Doit jouer le coup gagnant si il existe
        """

        next_grille = None
        A = self.Grille
        while next_grille is None:
            token = A.who_s_playing_after()
            if self.couleur != token:
                next_grille = A
                break
            Config_gagnante = A.est_gagnante()
            indice = -1
            res = None
            while token != res:
                try:
                    res = next(Config_gagnante)
                    indice += 1
                except StopIteration:
                    break
            if token == res:
                next_grille = A.add_token(indice, token)
                break
            next_grille = super().play()
        return next_grille
