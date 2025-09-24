from Grille import Grille

from Joueur import Joueur

from JoueurHumain import JoueurHumain

from random import random


def Partie_puissance4(Joueur1=False, Joueur2=False):
    """
    Lance une partie de Puissance 4 entre deux joueurs.

    Args:
        Joueur1 (bool, optional): Si True, le premier joueur est un joueur humain (JoueurHumain).
                                  Sinon, il s'agit d'un joueur automatique (Joueur).
                                  Par défaut False.
        Joueur2 (bool, optional): Si True, le second joueur est un joueur humain (JoueurHumain).
                                  Sinon, il s'agit d'un joueur automatique (Joueur).
                                  Par défaut False.

    Description:
        - Initialise une nouvelle grille de jeu.
        - Crée deux joueurs selon les paramètres spécifiés.
        - Alterne les tours de jeu entre les deux joueurs jusqu'à ce que la partie se termine.
        - Affiche l'état de la grille après chaque coup du second joueur.
        - La partie s'arrête dès qu'un joueur gagne ou que la grille est pleine.

    Returns:
        bool | str | None:
            - True si le joueur avec la couleur True gagne,
            - False si le joueur avec la couleur False gagne,
            - "impossible de finir" si la grille est pleine sans gagnant,
            - None si la partie est toujours en cours (cas très rare ici car la boucle s'arrête).
    """

    A = Grille()
    if Joueur1:
        J1 = JoueurHumain(A, True)
    else:
        J1 = Joueur(A, True)
    if Joueur2:
        J2 = JoueurHumain(A, False)
    else:
        J2 = Joueur(A, False)

    beginner = random()
    print(
        "Le premier à jouer est tirer au sort au pile ou face "
        "avec une pièce supposée équilibrée "
    )
    res = input("Appuyez sur n'importe quel caractère pour démarrer:")
    if res is not None:
        if beginner < 1 / 2:
            print("Joueur 1 commence")
            while not isinstance(A.Check(), bool) and not isinstance(A.Check(), str):
                J1.play()
                print(A)
                if isinstance(A.Check(), bool) or isinstance(A.Check(), str):
                    break
                J2.play()
                print(A)
        else:
            print("Joueur 2 commence")
            while not isinstance(A.Check(), bool) and not isinstance(A.Check(), str):
                J2.play()
                print(A)
                if isinstance(A.Check(), bool) or isinstance(A.Check(), str):
                    break
                J1.play()
                print(A)
        res = A.Check() + False
        if res == 0:
            res += 2
        print(f"Joueur {res} a gagné")
        return A.Check()
    else:
        raise TypeError("Votre entrée n'est pas valide")


def puissance4_simu():
    """
     Simule une partie de Puissance 4 entre deux joueurs.

    Description :
        - Initialise une nouvelle grille de jeu.
        - Crée deux joueurs (actuellement deux joueurs humains par défaut).
        - Alterne les tours entre les joueurs jusqu'à ce qu'un joueur gagne ou que la grille soit pleine.
        - La partie s'arrête dès qu'un gagnant est détecté ou que la grille ne peut plus accueillir de jetons.
        - Retourne le résultat de la partie.

    Returns:
        bool | str | None:
            - True si le joueur avec la couleur True gagne,
            - False si le joueur avec la couleur False gagne,
            - "impossible de finir" si la grille est pleine sans gagnant,

    Raises:
        TypeError: Si un état invalide est rencontré dans la partie (rare).
    """
    A = Grille()
    J1 = Joueur(A, True)
    J2 = Joueur(A, False)
    beginner = random()
    if beginner < 1 / 2:
        while not isinstance(A.Check(), bool) and not isinstance(A.Check(), str):
            J1.play()
            if isinstance(A.Check(), bool) or isinstance(A.Check(), str):
                break
            J2.play()
    else:
        while not isinstance(A.Check(), bool) and not isinstance(A.Check(), str):
            J2.play()
            if isinstance(A.Check(), bool) or isinstance(A.Check(), str):
                break
            J1.play()
    if isinstance(A.Check(), str):
        return A.Check()
    res = A.Check() + False
    if res == 0:
        res += 2
    return A.Check()
