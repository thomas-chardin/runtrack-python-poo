class Livre():
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
    def modifierTitre(self, titre):
        self.titre = titre
    def modifierAuteur(self, auteur):
        self.auteur = auteur
    def modifierPages(self, pages):
        if pages > 0 and type(pages) == int:
            self.pages = pages
        else:
            print("la donnée rentrée n'est pas un chiffre entier positif")
    def afficherTitre(self):
        print(f"le titre du livre est {self.titre}")
    def afficherAuteur(self):
        print(f"Le nom de l'auteur est {self.auteur}")
    def afficherPages(self):
        print(f"Le nombre de pages de ce livre est de {self.pages}")
    def vérification(self):
        if self.__disponible == True:
            return True
        else :
            return False
    def emprunter(self):
        if self.vérification() == True:
            self.__disponible = False
        else : 
            print("Ce livre est deja emprunter")
    def rendre(self):
        if self.vérification() == False:
            self.__disponible = True
        else : 
            print("Ce livre est deja disponible") 
livre = Livre("test", "thomas", 1)
livre.modifierPages(8)
livre.afficherPages()
livre.modifierPages(-10)
livre.modifierPages(1.6)

