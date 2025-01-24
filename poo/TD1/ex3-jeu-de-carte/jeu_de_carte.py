from enum import Enum
from random import shuffle
from typing import Union

from prompt_toolkit.key_binding.bindings.named_commands import capitalize_word


class Couleur(Enum):
    COEUR = 1
    CARREAU = 2
    PIQUE = 3
    TREFLE = 4

class Valeur(Enum):
    AS = 1
    DEUX = 2
    TROIS = 3
    QUATRE = 4
    CINQ = 5
    SIX = 6
    SEPT = 7
    HUIT = 8
    NEUF = 9
    DIX = 10
    VALET = 11
    REINE = 12
    ROI = 13

class Carte:
    def __init__(self, couleur: Couleur, valeur: Valeur):
        self.couleur = couleur
        self.valeur = valeur

    def __str__(self):
        return f"{self.valeur.name.title()} de {self.couleur.name.title()}"

class JeuDeCarte:
    def __init__(self):
        self.cartes = []
        for couleur in Couleur:
            for valeur in Valeur:
                self.cartes.append(Carte(couleur, valeur))

    @staticmethod
    def nom_carte(carte: Carte) -> None:
        print(carte)

    def battre(self) -> None:
        shuffle(self.cartes)

    def afficher(self) -> None:
        for carte in self.cartes:
            self.nom_carte(carte)

    def tirer(self) -> Union[Carte, None]:
        try:
            return self.cartes.pop()
        except IndexError:
            return None

if __name__ == '__main__':
    jeu = JeuDeCarte()
    jeu.battre()
    jeu.afficher()

    print("\n\nCommencer à tirer les cartes:\n")
    carte = jeu.tirer()
    while carte is not None:
        jeu.nom_carte(carte)
        carte = jeu.tirer()