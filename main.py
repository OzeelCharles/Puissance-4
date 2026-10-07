from src.game import Partie_v5
from src.game import Partie_v4
from src.game import Partie_v3
from src.game import Partie_v2
from src.game import Partie


lvl = 4


def main():
    if lvl == 4:
        return  Partie_v5.Partie_puissance4()
    elif lvl == 3: 
        return Partie_v4.Partie_puissance4()
    elif lvl == 2:
        return Partie_v3.Partie_puissance4()
    elif lvl == 1:
        return Partie_v2.Partie_puissance4()
    else:
        return Partie.Partie_puissance4()

if __name__ == "__main__":
    main()
