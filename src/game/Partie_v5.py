from src.interface.Configuration import Configuration
from src.players.JoueurNiveau2 import JoueurNiveau2
from src.players.JoueurNiveau4 import JoueurMinimax
from src.players.JoueurHumain import JoueurHumain
import random


def Partie_puissance4(J1=False, J2=False):
    grille = Configuration()
    j1 = JoueurHumain(grille, True) if J1 else JoueurNiveau2(grille, True)
    j2 = JoueurHumain(grille, False) if J2 else JoueurMinimax(grille, False)
    beginner = random.randint(0, 1)
    stop = 0
    while grille.Check() is None and stop < 10:
        if beginner == 1:
            grille = j1.play()
            print(grille)
            if grille.Check() is not None:
                break 
            grille = j2.play()
            print(grille)
        else:
            grille = j2.play()
            print(grille)
            if grille.Check() is not None:
                break   
            grille = j1.play()
            print(grille)
        stop += 1
    print(grille)
    return grille.Check()
