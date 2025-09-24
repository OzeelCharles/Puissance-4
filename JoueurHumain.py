from Joueur import Joueur


class JoueurHumain(Joueur):
    """
    Classe représentant un joueur humain, héritée de Joueur.

    Cette classe permet à un joueur humain de jouer en choisissant une colonne via une entrée utilisateur,
    et de gérer une partie complète opposant ce joueur à un joueur automatique (IA basique).
    """

    def play(self):
        """
        Permet au joueur humain de jouer un coup.

        Si la partie est terminée (selon la méthode Check de la grille), retourne la grille actuelle.
        Sinon, demande à l'utilisateur de saisir une colonne dans laquelle jouer, puis ajoute un jeton
        de la couleur du joueur dans cette colonne.

        Returns:
            Grille: La nouvelle grille mise à jour après l'ajout du jeton, ou la grille inchangée si la partie est terminée.
        """
        if self.Grille.Check() != None:
            return self.Grille
        print("choississez une Colonne où jouer")
        k = input()
        return self.Grille.ajout_jeton(int(k), self.couleur)
