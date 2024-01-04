class Voiture():
    def __init__(self,marque, année,modéle, kilométrage):
        self.__marque = marque
        self.__année = année
        self.__modéle = modéle
        self.__kilométrage = kilométrage
        self.__reservoir = 50
        self.__en_marche = False
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modéle
    def get_annee(self):
        return self.__année
    def get_kilometrage(self):
        return self.__kilométrage
    def get_en_marche(self):
        return self.__en_marche
    def set_marque(self,marque):
        self.__marque = marque
    def set_modele(self, modéle):
        self.__modéle = modéle
    def set_annee(self, année):
        self.__année = année
    def set_kilometrage(self, kilométrage):
        self.__kilométrage = kilométrage
    def demarrer(self):
        if self.__reservoir > 5:
            self.__en_marche = True
    def arreter(self):
        self.__en_marche = False
    def __verifier_plein(self):
        return self.__reservoir
n = Voiture("Bmw", 2020,"série 8",10000)

n.demarrer()
print(n.get_en_marche())
n.arreter()
print(n.get_en_marche())

