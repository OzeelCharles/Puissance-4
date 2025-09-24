from random import randint
from random import choice
from JoueurNiveau1 import JoueurNiveauUn


class JoueurNiveauDeux(JoueurNiveauUn):

    def play_v2(self):
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

        while next_grille is None:
            jeton = self.Grille.who_s_playing_after()
            if self.couleur != jeton or self.Grille.Check() != None:
                next_grille = self.Grille
                break

            Config_gagnante = self.Grille.est_gagnante()
            indice = -1
            res = not jeton
            while jeton != res:
                try:
                    res = next(Config_gagnante)
                    indice += 1

                except StopIteration:
                    break

            if jeton == res:
                A = self.Grille.copy()
                next_grille = A.ajout_jeton(indice, jeton)
                if A.Grille != self.Grille:
                    next_grille = self.Grille.ajout_jeton(indice, jeton)
                    break
            
            # Si ce if ne s'active c'est qu'il n'y a pas de victoire pour l'autre joueur
 
            Config_suivante = self.Grille.configuration_suivante()
            playable_indice = None
            while playable_indice is None:
                try:
                    Config = next(Config_suivante)
                    Config_gagnante_adv = Config.Grille.est_gagnante()
                    jeton_2 = not jeton
                    res = not jeton_2
                    indice_adv = 0
                    list_not_adv = list(range(7))
                    while indice_adv < 7:
                        try:
                            res = next(Config_gagnante_adv)
                            indice_adv += 1
                            if res == jeton_2:
                                list_not_adv.remove(indice_adv)
                        except StopIteration:
                            break
                    if list_not_adv != []:
                        rd = choice(list_not_adv)
                        playable_indice = list_not_adv[rd]
                        break

                except StopIteration:
                    break

                if playable_indice is not None:
                    next_grille = self.Grille.ajout_jeton(playable_indice, jeton)

                else:
                    next_grille = self.Grille.ajout_jeton(randint(0, 6), jeton)

        return next_grille
