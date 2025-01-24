from typing import Set


class Ville:
    def __init__(self, nom: str, nb_hab: int) -> None:
        self.__nom = nom
        self.__nb_hab = nb_hab

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def nb_hab(self) -> int:
        return self.__nb_hab

    @nb_hab.setter
    def nb_hab(self, nb_hab: int) -> None:
        if nb_hab < 0:
            raise ValueError("Le nombre d'habitants ne peut pas être négatif")
        self.__nb_hab = nb_hab

    def __str__(self) -> str:
        return f"{self.__nom} - Nombre d'habitant: {self.__nb_hab}"


class Capitale(Ville):
    def __init__(self, nom: str, nb_hab: int) -> None:
        super().__init__(nom, nb_hab)
        self.__monuments: Set[str] = set()

    @property
    def monuments(self) -> Set[str]:
        return self.__monuments

    def add_monument(self, monument: str) -> None:
        if monument not in self.monuments:
            self.monuments.add(monument)

    def __str__(self) -> str:
        monuments_str = ", ".join(self.monuments) if self.monuments else "aucun"
        return f"{super().__str__()} - Monuments: {monuments_str}"


def test_ville():
    print("\n=== Testing Ville ===")
    ville = Ville("Paris", 2_000_000)
    print(ville)

    ville.nb_hab = 2_500_000
    print(f"After population update: {ville}")

    try:
        ville.nb_hab = -1
    except ValueError as e:
        print(f"Caught expected error: {e}")


def test_capitale():
    print("\n=== Testing Capitale ===")
    capitale = Capitale("London", 9_000_000)
    print(capitale)

    capitale.add_monument("Big Ben")
    capitale.add_monument("Tower Bridge")
    print(f"After adding monuments: {capitale}")

    # Test duplicate monument
    capitale.add_monument("Big Ben")
    print(f"After adding duplicate: {capitale}")


if __name__ == "__main__":
    test_ville()
    test_capitale()