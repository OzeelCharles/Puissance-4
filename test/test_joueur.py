import pytest as pt
from Grille import Grille

@pt.mark.parametrize("grille, couleur, res, error", [([], True, '[] n\'est pas un objet Grille'),
                                                     (joueur_grille, (), "() n\'est pas de type booléen"),
                                                     ()])
def test_joueur(grille, couleur, res, error):
    pass

