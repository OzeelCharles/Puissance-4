from interface.Configuration import Configuration
from players.Joueur import Joueur
from players.JoueurNiveau1 import JoueurNiveauUn
from players.JoueurHumain import JoueurHumain
import random


def Partie_puissance4(J1=False, J2=False):
    grille = Configuration()
    j1 = JoueurHumain(grille, True) if J1 else Joueur(grille, True)
    j2 = JoueurHumain(grille, False) if J2 else JoueurNiveauUn(grille, False)
    beginner = random.randint(0, 1)
    while grille.Check() is None:
        if beginner == 1:
            j1.play()
            print(grille)
            j2.play()
            print(grille)
        else:
            j2.play()
            print(grille)
            j1.play()
            print(grille)
    print(grille)
    return grille.Check()
