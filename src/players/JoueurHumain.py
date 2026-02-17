from players.Joueur import Joueur


class JoueurHumain(Joueur):
    """
    Classe représentant un joueur humain, héritée de Joueur.

    Cette classe permet à un joueur humain de jouer en choisissant
    une colonne via une entrée utilisateur
    """

    def play(self):
        if self.Grille.Check() is not None:
            return self.Grille
        k = input("choississez une Colonne où jouer:  ")
        return self.Grille.add_token(int(k), self.couleur)
