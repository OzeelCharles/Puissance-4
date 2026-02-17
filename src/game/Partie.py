from interface.Grille import Grille
from players.Joueur import Joueur
from players.JoueurHumain import JoueurHumain
import random


def Partie_puissance4(J1=False, J2=False):
    grille = Grille()
    J1 = JoueurHumain(grille, True) if J1 else Joueur(grille, True)
    J2 = JoueurHumain(grille, False) if J2 else Joueur(grille, False)
    beginner = random.randint(0, 1)
    while grille.Check() is None:
        if beginner == 1:
            J1.play()
            print(grille)
            J2.play()
            print(grille)
        else:
            J2.play()
            print(grille)
            J1.play()
            print(grille)
    print(grille)
    return grille.Check()
