# Modélisation de la classe Grille#


class Grille:
    """
    Classe représentant une grille de jeu vide, structurée en 6 lignes et 7 colonnes.

    Cette grille est typiquement utilisée pour des jeux comme le Puissance 4.

    Attributs :
    - La grille est stockée localement dans la méthode __init__ sous forme d’un tuple de tuples,
      où chaque cellule est initialisée à None (cellule vide).

    """

    def __init__(self):
        grille_data = ()
        """
        Initialise une grille vide de 6 lignes par 7 colonnes.

        Chaque cellule est représentée par la valeur None, et la grille est construite
        en utilisant des tuples imbriqués pour garantir l'immuabilité.
        """
        grille_data = tuple(tuple(None for i in range(7)) for j in range(6))
        self.Grille = grille_data

    def __repr__(self):
        """
        Retourne une représentation textuelle de la grille.

        Cette méthode génère une chaîne de caractères contenant chaque ligne de la grille
        sur une nouvelle ligne. Elle suppose que la grille est stockée dans l'attribut `self.Grille`.

        Returns:
            str: Représentation ligne par ligne de la grille.
        """
        res = ""
        for i in range(len(self.Grille)):
            res += f"{str(self.Grille[i])}"
            res += "\n"
        return res

    def ajout_jeton(self, colonne: int, Couleur: bool):
        """
        Ajoute un jeton de la couleur donnée dans la colonne spécifiée.

        Le jeton descend jusqu’à la première case vide (de bas en haut).
        Si la colonne est pleine, la grille reste inchangée.

        Args:
            colonne (int): L’indice de la colonne (0 à 6).
            Couleur (bool): La couleur du jeton (par exemple True pour rouge, False pour jaune).

        Returns:
            self: L’instance de Grille mise à jour.
        """
        if colonne < 0 or colonne > 6:
            raise ValueError(f"{colonne} n'est pas compris entre 0 et 6.")
        if not isinstance(Couleur, bool):
            raise TypeError(f"Couleur doit être un booléen, pas {type(Couleur).__name__}")
    
        line = 5
        while line > -1:
            if self.Grille[line][colonne] is None:
                new_line = tuple(
                    Couleur if col == colonne else self.Grille[line][col]
                    for col in range(7)
                )
                self.Grille = tuple(
                    new_line if i == line else self.Grille[i] for i in range(6)
                )
                break
            if line == 0 and (self.Grille[line][colonne] is not None):
                print("Tableau plein sur cette colonne")
                break
            line -= 1
        return self

    def check_True(self):
        """
        Vérifie si un joueur représenté par True (par exemple, jetons rouge) a gagné.

        Returns:
            bool | None: True si une séquence gagnante est détectée, sinon None.
        """
        for ligne in range(6):
            for colonne in range(7):
                if self.Grille[ligne][colonne] != True:
                    continue

                # Vérifie horizontalement vers la droite
                if colonne <= 3 and all(
                    self.Grille[ligne][colonne + i] == True for i in range(4)
                ):
                    return True

                # Vérifie verticalement vers le bas
                if ligne <= 2 and all(
                    self.Grille[ligne + i][colonne] == True for i in range(4)
                ):
                    return True

                # Vérifie diagonale descendante (\)
                if (
                    ligne <= 2
                    and colonne <= 3
                    and all(
                        self.Grille[ligne + i][colonne + i] == True for i in range(4)
                    )
                ):
                    return True

                # Vérifie diagonale montante (/)
                if (
                    ligne >= 3
                    and colonne <= 3
                    and all(
                        self.Grille[ligne - i][colonne + i] == True for i in range(4)
                    )
                ):
                    return True

        return None

    def check_False(self):
        """
        Vérifie si un joueur représenté par False (par exemple, jetons jaunes) a gagné.

        Returns:
            bool | None: False si une séquence gagnante est détectée, sinon None.
        """
        for ligne in range(6):
            for colonne in range(7):
                if self.Grille[ligne][colonne] == True:
                    continue

                # Vérifie horizontalement vers la droite
                if colonne <= 3 and all(
                    self.Grille[ligne][colonne + i] == False for i in range(4)
                ):
                    return False

                # Vérifie verticalement vers le bas
                if ligne <= 2 and all(
                    self.Grille[ligne + i][colonne] == False for i in range(4)
                ):
                    return False

                # Vérifie diagonale descendante (\)
                if (
                    ligne <= 2
                    and colonne <= 3
                    and all(
                        self.Grille[ligne + i][colonne + i] == False for i in range(4)
                    )
                ):
                    return False

                # Vérifie diagonale montante (/)
                if (
                    ligne >= 3
                    and colonne <= 3
                    and all(
                        self.Grille[ligne - i][colonne + i] == False for i in range(4)
                    )
                ):
                    return False

        return None

    def Check(self):
        """
        Vérifie l'état actuel de la partie dans la grille.

        - Compte le nombre de colonnes pleines à la première ligne (indice 0).
        - Si toutes les colonnes de la première ligne sont occupées (aucune case None),
          cela signifie que la grille est pleine et qu'il est impossible de continuer la partie.
          Dans ce cas, retourne la chaîne de caractères "impossible de finir".
        - Sinon, vérifie si le joueur avec les jetons True a gagné en appelant self.check_True().
        - Si aucun joueur True n'a gagné, vérifie si le joueur avec les jetons False a gagné en appelant self.check_False().
        - Retourne le résultat de ces vérifications :
            - True si le joueur True a gagné,
            - False si le joueur False a gagné,
            - None si aucun joueur n'a encore gagné.

        Returns:
            str | bool | None:
                - "impossible de finir" si la grille est pleine,
                - True si le joueur True a gagné,
                - False si le joueur False a gagné,
                - None sinon.
        """
        verif = 0
        for colonne in range(7):
            if self.Grille[0][colonne] is not None:
                verif += 1
        if verif == 7:
            print(repr(self))
            return "tableau plein, impossible de finir"
                
        return self.check_True() or self.check_False()
