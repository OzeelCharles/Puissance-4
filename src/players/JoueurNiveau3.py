from players.Joueur import Joueur


class JoueurNiveauTrois(Joueur):

    def play_v2(self):
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
        if reverse != []:
            return A.add_token(
                reverse[0], token)
        res_counter = A.est_gagnante2()
        for indice, _ in enumerate(range(7)):
            if not next(res_counter):
                return A.add_token(indice, token)
        return super().play()
