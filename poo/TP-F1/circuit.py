import random

from overrides import overrides


class DepassementError(Exception):
    pass


class F1:
    def __init__(self, moteur: int, temperature_pneumatique: int, vitesse: int, position: int) -> None:
        self.__moteur = moteur
        self.__temperature_pneumatique = temperature_pneumatique
        self.__vitesse = vitesse
        self.__position = position
        self.__drs = False

    @property
    def temperature_pneumatique(self) -> int:
        return self.__temperature_pneumatique

    @temperature_pneumatique.setter
    def temperature_pneumatique(self, temperature_pneumatique: int) -> None:
        self.__temperature_pneumatique = temperature_pneumatique

    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int) -> None:
        self.__position = position

    @property
    def temperature_moteur(self) -> float:
        return self.__temperature_pneumatique * 0.09 * self.__vitesse * 0.11

    def moteur_is_dead(self):
        return self.temperature_moteur <= 360

    def accelerer(self, acceleration):
        self.__vitesse += acceleration * 1.15 if self.__drs else 1

    def toggle_drs(self):
        self.__drs = not self.__drs

    def depassement(self, f1_depasse: 'F1'):
        if f1_depasse.position != self.__position - 1:
            raise DepassementError("Une F1 ne peut dépasser que la F1 devant elle")

        self.__position -= 1
        f1_depasse.position += 1

    def __str__(self):
        return f"<Position: {self.__position} - Moteur: {self.__moteur} - Temp. Pneu.: {self.__temperature_pneumatique} - Vit.: {self.__vitesse} - DRS. On: {self.__drs}>"


class F1Redbull(F1):
    def __init__(self, moteur: int, temperature_pneumatique: int, vitesse: int, position: int) -> None:
        super().__init__(moteur, temperature_pneumatique, vitesse, position)

    @overrides
    def depassement(self, f1_depasse: 'F1'):
        super().depassement(f1_depasse)

        self.temperature_pneumatique -= self.temperature_pneumatique * 0.08
        if isinstance(f1_depasse, F1Mercedes):
            f1_depasse.temperature_pneumatique += f1_depasse.temperature_pneumatique * 0.12
        elif isinstance(f1_depasse, F1Ferrari):
            f1_depasse.temperature_pneumatique += f1_depasse.temperature_pneumatique * 0.14
            f1_depasse.accelerer(random.randint(5, 12) * -1)


class F1Mercedes(F1):
    def __init__(self, moteur: int, temperature_pneumatique: int, vitesse: int, position: int) -> None:
        super().__init__(moteur, temperature_pneumatique, vitesse, position)

    @overrides
    def depassement(self, f1_depasse: 'F1'):
        super().depassement(f1_depasse)
        self.temperature_pneumatique -= self.temperature_pneumatique * 0.11
        if isinstance(f1_depasse, F1Ferrari):
            f1_depasse.accelerer(random.randint(5, 12) * -1)


class F1Ferrari(F1):
    def __init__(self, moteur: int, temperature_pneumatique: int, vitesse: int, position: int) -> None:
        super().__init__(moteur, temperature_pneumatique, vitesse, position)


if __name__ == "__main__":
    # Création des voitures
    ferrari = F1Ferrari(moteur=900, temperature_pneumatique=80, vitesse=280, position=3)
    mercedes = F1Mercedes(moteur=950, temperature_pneumatique=85, vitesse=290, position=2)
    redbull = F1Redbull(moteur=980, temperature_pneumatique=82, vitesse=295, position=1)

    print("Positions de départ:")
    print(redbull)
    print(mercedes)
    print(ferrari)

    # Premier dépassement
    ferrari.accelerer(20)
    ferrari.toggle_drs()
    ferrari.depassement(mercedes)

    print("\nAprès premier dépassement:")
    print(redbull)
    print(ferrari)
    print(mercedes)

    # Deuxième dépassement
    redbull.accelerer(15)
    ferrari.accelerer(30)  # Ferrari pousse son moteur
    ferrari.depassement(redbull)

    print("\nAprès deuxième dépassement:")
    print(ferrari)
    print(redbull)
    print(mercedes)

    # Vérification état moteur Ferrari
    print(f"\nTempérature moteur Ferrari: {ferrari.temperature_moteur:.2f}")
    print(f"Moteur Ferrari en panne: {ferrari.moteur_is_dead()}")
