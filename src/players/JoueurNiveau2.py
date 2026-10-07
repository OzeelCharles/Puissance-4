from src.players.Joueur import Joueur


class JoueurNiveau2(Joueur):
    def play(self):
        """
        Doit jouer le coup gagnant si il existe,
        sinon joue le coup gagnant de l'adversaire si il existe,
        sinon joue aléatoirement
        """
        
        A = self.Grille
        token = A.who_s_playing_after()
        if self.couleur != token:
            return A
        Config_gagnante = A.est_gagnante()
        indice = -1
        res = None
        reverse = []
        while not isinstance(res, bool) and indice < 6:
            try:
                res = next(Config_gagnante)
                indice += 1
                if not isinstance(res, type(None)) and res is not token:
                    reverse.append(indice)
            except StopIteration:
                break
        if token == res:
            return A.add_token(indice, token)
        return A.add_token(
            reverse[0], token) if reverse != [] else super().play()
