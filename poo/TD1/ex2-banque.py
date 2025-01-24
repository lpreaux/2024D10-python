
class CompteBancaire:
    TAUX_COMMISSION = 0.05;

    def __init__(self, numero_compte: int, titulaire: str, solde: float):
        self.numero_compte = numero_compte
        self.titulaire = titulaire
        self.solde = solde

    def depot(self, montant: float):
        self.solde += montant

    def retrait(self, montant: float):
        self.solde -= montant

    def comission(self):
        self.solde -= self.solde * self.TAUX_COMMISSION

    def afficher(self):
        print(f"Compte {self.numero_compte}: Titulaire: {self.titulaire}, solde: {self.solde}")

if __name__ == '__main__':
    compte = CompteBancaire(1, "John Doe", 1000)
    compte.afficher()
    compte.depot(200)
    compte.afficher()
    compte.retrait(50)
    compte.afficher()
    compte.comission()
    compte.afficher()


## Pour plus de précision il est possible d'utiliser le wrapper `Decimal` qui garantie la précision :
from decimal import Decimal

class CompteBancaire:
    TAUX_COMMISSION = Decimal('0.05')

    def __init__(self, numero_compte: int, titulaire: str, solde: Decimal):
        self.numero_compte = numero_compte
        self.titulaire = titulaire
        self.solde = Decimal(str(solde))

    def deposer(self, montant: Decimal) -> None:
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif")
        self.solde += Decimal(str(montant))

    def retirer(self, montant: Decimal) -> None:
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif")
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= Decimal(str(montant))

    def appliquer_commission(self) -> None:
        self.solde -= self.solde * self.TAUX_COMMISSION

    def afficher(self) -> None:
        print(f"Compte {self.numero_compte}: Titulaire: {self.titulaire}, Solde: {self.solde:.2f}")

if __name__ == '__main__':
    compte = CompteBancaire(1, "Jean Dupont", Decimal('1000.00'))
    compte.afficher()
    compte.deposer(Decimal('200.00'))
    compte.afficher()
    compte.retirer(Decimal('50.00'))
    compte.afficher()
    compte.appliquer_commission()
    compte.afficher()
