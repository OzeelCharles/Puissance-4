# Modélisation de la classe Grille#
from itertools import product
import copy


class Grille:

    def __init__(self):
        grille = [[None for _ in range(7)] for _ in range(6)]
        self.Grille = grille

    def __repr__(self):
        res = ""
        for i in range(len(self.Grille)):
            res += f"{str(self.Grille[i])}"
            res += "\n"
        return res

    def __eq__(self, grille):
        if not isinstance(grille, Grille):
            raise ValueError
        return self.Grille == grille.Grille

    def copy(self):
        cop = Grille()
        cop.Grille = copy.deepcopy(self.Grille)
        return cop

    def check_True(self):
        for ligne, colonne in product(range(6), range(7)):
            if not self.Grille[ligne][colonne]:
                continue
            if (
                colonne <= 3
                and all(self.Grille[ligne][colonne + i] for i in range(4))
            ):
                return True
            if (
                ligne <= 2
                and all(self.Grille[ligne + i][colonne] for i in range(4))
            ):
                return True
            if (
                ligne <= 2
                and colonne <= 3
                and all(self.Grille[ligne + i][colonne + i] for i in range(4))
            ):
                return True
            if (
                ligne >= 3
                and colonne <= 3
                and all(self.Grille[ligne - i][colonne + i] for i in range(4))
            ):
                return True
        return None

    def check_False(self):
        for ligne, colonne in product(range(6), range(7)):
            if self.Grille[ligne][colonne] is not False:
                continue
            if colonne <= 3 and all(
                self.Grille[ligne][colonne + i] is False for i in range(4)
            ):
                return False
            if ligne <= 2 and all(
                self.Grille[ligne + i][colonne] is False for i in range(4)
            ):
                return False
            if (
                ligne <= 2
                and colonne <= 3
                and all(
                    self.Grille[ligne + i][colonne + i]
                    is False for i in range(4))
            ):
                return False
            if (
                ligne >= 3
                and colonne <= 3
                and all(
                    self.Grille[ligne - i][colonne + i]
                    is False for i in range(4))
            ):
                return False
        return None

    def Check(self):
        full_condi = set(self.Grille[0])
        if not {None}.issubset(full_condi):
            return "full"
        val = self.check_False()
        return self.check_True() if val is None else val

    def add_token(self, colonne: int, Couleur: bool):
        if colonne < 0 or colonne > 6:
            raise ValueError(f"{colonne} n'est pas compris entre 0 et 6.")
        if not isinstance(Couleur, bool):
            raise TypeError(
                f"Couleur doit être un booléen, pas {type(Couleur).__name__}"
            )
        if self.Check() is not None:
            return self
        line = 5
        while line > -1:
            if self.Grille[line][colonne] is None:
                new_line = [
                    Couleur if col == colonne else self.Grille[line][col]
                    for col in range(7)
                ]
                self.Grille = [
                    new_line if i == line else self.Grille[i] for i in range(6)
                ]
                break
            line -= 1
        if line < 0:
            print("Tableau plein sur cette colonne")
        return self
