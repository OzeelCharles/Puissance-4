# Classe joueur artificiel#

import interface.Grille as Grille
import interface.Configuration as Configuration
import random


class Joueur:
    """
    Représente un joueur dans le jeu,
    qui joue avec une couleur spécifique sur une grille donnée.

    Attributes:
        grille (Grille): La grille de jeu sur laquelle le joueur joue.
        couleur (bool): La couleur du joueur (par exemple True ou False).
    """

    def __init__(self, grille: Grille, couleur: bool):
        if not isinstance(
            grille, Grille.Grille) or not isinstance(
                grille, Configuration.Configuration):
            raise TypeError(f"{grille} n'est pas un objet Grille")
        if not isinstance(couleur, bool):
            raise TypeError(f"{couleur} n'est pas de type booléen")
        self.Grille = grille
        self.couleur = couleur

    def play(self):
        next_grille = None
        value = random.randint(0, 6)
        while next_grille is None:
            val = self.Grille.Check()
            next_grille = self.Grille.add_token(
                value, self.couleur) if val is None else self.Grille
        return next_grille
