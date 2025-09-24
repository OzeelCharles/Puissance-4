from Grille import Grille


class Configuration(Grille):

    def who_s_playing_after(self):
        """
        Prédicat renvoyant le booléen associé au joueur suivant devant joueur.
        Return:
        Bool: True si c'est au joueur 1 de jouer, False sinon si c'est au joueur 2
        """
        res = 0
        for ligne in range(len(self.Grille)):
            for colonne in range(len(self.Grille[ligne])):
                if self.Grille[ligne][colonne] == True:
                    res += True
                elif self.Grille[ligne][colonne] == False:
                    res -= True
                else:
                    None

        if res == 1:
            return False
        elif res == 0:
            return True
        else:
            if res < 0:
                raise ValueError( "Triche de False")
            else:
                raise ValueError("Triche de True")

    def copy(self):
        """
        Renvoie une copie de l'instance avec même grille
        Cette grille ne sera pas changer si l'instance change.
        return:
        Configuration: Configuration avec un attribut Grille identique à l'instance
        """
        B = Configuration()
        B.Grille = tuple(self.Grille)
        return B

    def configuration_suivante(self):
        """
        génère eun objet configuration issu de l'instance avec un jeton en plus
        Permettant de générer l'ensemble des configuration possible issu de l'instance.
        Args:
        start = 0
        end = 7
        Yield:
        Configuration: Configuration avec un jeton ajouté sur les combinaisons utiles
        """
        jeton = self.who_s_playing_after()
        i = 0
        while i < 7:
            B = self.copy()
            B.ajout_jeton(i, jeton)
            yield B
            i += 1

    def est_gagnante(self):
        """
        génère une suite de booléen correspondant à l'état "est gagnante" des configurations issus du générateur configuration_suivante
        Arg:
        start = 0
        end = 7
        Yield:
        Bool: True si la configuratione est gagné par Joueur1, False sinon
        NoneType: None si il n'y a pas de vainqueurs
        """
        config = self.configuration_suivante()
        i = 0
        while i < 7:
            yield next(config).Check()
            i += 1

    def apres(self):
        config = self.configuration_suivante()
        i = 0
        while i < 7:
            yield next(config).configuration_suivante()
            i += 1

    # Créer générateur des configurations suivantes des configs suivantes (donc 7 listes de 7 config possible) #

    def apres2(self):
        config = self.apres()
        i = 0
        while i < 7:
            j = 0
            config_2 = next(config)
            while j < 7:
                yield list(next(config_2).est_gagnante())
                j += 1
            i += 1

        # Créer un générateur d'au plus 49 liste de config gagnante ou non#

    def config_possiblement_gagnante(self):
        jeton = self.who_s_playing_after()
        config = self.apres2()
        i = 0
        while i < 49:
            if jeton in next(config):
                return True
            i += 1
        return False

    def config_virtuellement_gagnante(self, a=0):
        jeton = self.who_s_playing_after()
        if self.config_possiblement_gagnante():
            return True
        B = self.copy()
        B.ajout_jeton(a, jeton)
        B.ajout_jeton(a, jeton).ajout_jeton(a, jeton)

        # PB: je dois faire jouer True et False dans les 49 positions possibles pour leurs applqieur ensuite la boucle #
