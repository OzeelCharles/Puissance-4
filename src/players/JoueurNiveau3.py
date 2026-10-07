from src.players.Joueur import Joueur
from random import choice

class JoueurNiveau3(Joueur):
    def play(self):
        """
        Doit jouer le coup gagnant si il existe,
        sinon joue le coup gagnant de l'adversaire si il existe,
        sinon regarde selon le coup adverse possible quelle coup peut amener à une victoire, 
        Si il existe plus de deux solutions (Fourchette), on joue ce coup et s'assure une victoire
        Si il existe une seule solution on la joue quand même en espérant
        Si il existe que des coups qui n'amènent pas à une défaite au coup suivant on le joue
        Sinon on joue aléatoirement
        """
        A = self.Grille
        token = A.who_s_playing_after()
        if self.couleur != token:
            return A
        
        mes_victoires, victoires_adverses = A.analyse_grille(token)
        if mes_victoires:
            return A.add_token(mes_victoires[0], token)
        if victoires_adverses:
            return A.add_token(victoires_adverses[0], token)
        
        coups_surs = []
        coup_fourchette = None

        generateur_configs = A.copy().config_suivante(token)
        
        for col in range(7):
            try:
                A_sim = next(generateur_configs)
            except StopIteration:
                break

            if A_sim is None: 
                continue
            victoires_adv_apres_mon_coup, _ = A_sim.analyse_grille(not token)
            if not victoires_adv_apres_mon_coup:
                coups_surs.append(col)
                nos_victoires_futures, _ = A_sim.analyse_grille(token)
                if len(nos_victoires_futures) >= 2:
                    coup_fourchette = col
                    break

        if coup_fourchette is not None:
            return A.add_token(coup_fourchette, token)
        if coups_surs:
            return A.add_token(choice(coups_surs), token)
        return super().play()