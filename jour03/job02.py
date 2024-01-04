class CompteBancaire():
    def __init__(self,numéro_de_compte, nom, prénom,solde):
        self.__numéro_de_compte = numéro_de_compte
        self.__nom = nom
        self.__prénom = prénom
        self.__solde = solde
        self.__découvert = False
    def afficher(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prénom}")
        print(f"Solde : {self.__solde} €")
    def afficher_solde(self):
        print(f"Votre solde est de : {self.__solde} €")
    def versements(self,montant_versement):
        self.__solde += montant_versement
    def retrait(self,retrait):
        if retrait <= self.__solde or self.__découvert == True:
            self.__solde -= retrait
            print(f"Votre solde est de {self.__solde} €")
            if self.__solde < 0:
                self.agios()
                print("Nous vous avons prélevés 6€ pour votre découvert")
        elif self.__découvert == False:
            print("Vous n'avez pas le droit au decouvert")
        else:
            print("Vous n'avez pas le solde suffisant")
    def agios(self):
        if self.__solde < 0:
            self.__solde -= 6
    def virement(self, montant_virement, compte_cible):
        if 0 < montant_virement:
            self.__solde -= montant_virement
            compte_cible.versements(montant_virement)
        else:
            print("Montant invalide")



n = CompteBancaire(1,"Abdelkrim","Edine",2000)
y = CompteBancaire(2,"Abdelkrim","Tensel",-100)
n.afficher()
n.afficher_solde()
n.versements(100)
n.afficher_solde()
n.retrait(100)
n.afficher_solde()
n.retrait(2100)
n.afficher_solde()
y.afficher()
n.virement(100,y)
n.afficher_solde()
y.afficher_solde()




