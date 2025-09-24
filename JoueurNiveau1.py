from Joueur import Joueur
from random import randint


class JoueurNiveauUn(Joueur):

    def play(self):
        """
        Joue un coup pour le joueur courant selon une stratégie simple.

        Cette méthode effectue un coup dans la grille de jeu en suivant les étapes suivantes :
        - Vérifie si c'est au tour de ce joueur de jouer. Si ce n'est pas le cas, elle retourne la grille inchangée.
        - Tente de détecter une configuration gagnante possible en simulant les coups via un générateur.
        - Si une configuration gagnante est trouvée pour ce joueur, elle joue le coup correspondant.
        - Sinon, elle joue un coup aléatoire dans une colonne valide.

        Returns:
            Grille: Une nouvelle grille mise à jour après que le coup a été joué.
        """
        next_grille = None

        A = self.Grille

        while next_grille is None:

            jeton = A.who_s_playing_after()

            if self.couleur != jeton or A.Check() != None:
                next_grille = A
                break

            Config_gagnante = A.est_gagnante()

            indice = -1

            res = not jeton

            while jeton != res:
                try:
                    res = next(Config_gagnante)
                    indice += 1

                except StopIteration:
                    break
            

            if jeton == res:
                next_grille = A.ajout_jeton(indice, jeton)
                break 
            
            next_grille = A.ajout_jeton(randint(0, 6), self.couleur)


        return next_grille
