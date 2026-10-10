from src.players.Joueur import Joueur
from random import choice
import math

class JoueurMinimax(Joueur):
    """
    Joueur absolu optimisé par MINIMAX.
    """
    
    def __init__(self, grille, couleur, profondeur_max=4):
        super().__init__(grille, couleur)
        self.profondeur_max = profondeur_max

    
    def minimax(self, grille, profondeur, maximisant, token, alpha=-math.inf, beta=math.inf):
        adversaire = not token
        gagnant = grille.Check()
        
        if gagnant == token:
            return 10000 + profondeur
        elif gagnant == adversaire:
            return -10000 - profondeur
            
        if profondeur == 0:
            return grille.evaluer_plateau(token)

        if maximisant:
            max_eval = -math.inf
            generateur = grille.config_suivante(token)
            
            for _ in range(7):
                try:
                    enfant = next(generateur)
                    if enfant is None: 
                        continue
                    eval = self.minimax(enfant, profondeur - 1, False, token, alpha, beta)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break 
                except StopIteration:
                    break
            return max_eval
            
        else:
            min_eval = math.inf
            generateur = grille.config_suivante(adversaire)
            for _ in range(7):
                try:
                    enfant = next(generateur)
                    if enfant is None: 
                        continue
                    eval = self.minimax(enfant, profondeur - 1, True, token, alpha, beta)
                    min_eval = min(min_eval, eval)  
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break 
                except StopIteration:
                    break
            return min_eval


def play(self):
        A = self.Grille
        my_token = A.who_s_playing_after()
        if self.couleur != my_token:
            return A
        
        meilleur_score = -math.inf
        meilleur_coup = None
        coups_egalites = [] 
        generateur = A.config_suivante(my_token)
        for col in range(7):
            try:
                enfant = next(generateur)
                if enfant is None: continue
                score = self.minimax(grille=enfant, profondeur = self.profondeur_max - 1, maximisant=False, token = my_token)
                if meilleur_coup is None:
                    meilleur_coup = col
                if col == 3: score += 2
                elif col in [2, 4]: score += 1
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_coup = col
                    coups_egalites = [col]
                elif score == meilleur_score:
                    coups_egalites.append(col)  
            except StopIteration:
                break     
        choix_final = choice(coups_egalites) if coups_egalites else meilleur_coup
        if choix_final is None:
            return A
        nouvelle_grille = A.add_token(choix_final, my_token)
        if nouvelle_grille is None:
            colonnes_valides = [c for c in range(7) if A.Grille[0][c] is None]
            if colonnes_valides:
                colonne_aleatoire = choice(colonnes_valides)
                return A.add_token(colonne_aleatoire, my_token)
            return A  # Si vraiment toute la grille est pleine
            
        return nouvelle_grille

    