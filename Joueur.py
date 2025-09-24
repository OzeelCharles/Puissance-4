# Classe joueur artificiel#

import Grille
import random


class Joueur:
    """
    Représente un joueur dans le jeu, qui joue avec une couleur spécifique sur une grille donnée.

    Attributes:
        grille (Grille): La grille de jeu sur laquelle le joueur joue.
        couleur (bool): La couleur du joueur (par exemple True ou False).
    """

    def __init__(self, grille: Grille, couleur: bool):
        """
        Initialise un joueur avec une grille et une couleur.

        Args:
            grille (Grille): L'instance de la grille de jeu.
            couleur (bool): La couleur du joueur.
        """
        if not isinstance(grille, Grille.Grille):
            raise TypeError(f'{grille} n\'est pas un objet Grille')
        if not isinstance(couleur, bool):
            raise TypeError(f'{couleur} n\'est pas de type booléen')
        self.Grille = grille
        self.couleur = couleur

    def play(self):
        """
        Effectue un coup aléatoire sur la grille en ajoutant un jeton de la couleur du joueur.

        Tente aléatoirement d'ajouter un jeton dans une colonne (de 0 à 6) tant que le coup
        n'est pas valide (colonne pleine). Continue jusqu'à ce qu'un coup valide soit joué.

        Returns:
            Grille: La nouvelle grille mise à jour après l'ajout du jeton.
        """
        next_grille = None
        value = random.randint(0, 6)
        while next_grille is None:
            next_grille = self.Grille.ajout_jeton(value, self.couleur)
        return next_grille
