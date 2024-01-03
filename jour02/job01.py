class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    def changerLongueur(self, longueur):
        self.longueur = longueur
    def changerLargeur(self, largeur):
        self.largeur = largeur
    def afficherLongueur(self):
        print(f"la longueur du rectangle est de {self.longueur}")
    def afficherLargeur(self):
        print(f"la largeur du rectangle est de {self.largeur}")
rectangle = Rectangle(10, 5)
rectangle.changerLargeur(10)
rectangle.changerLongueur(20)
rectangle.afficherLargeur()
rectangle.afficherLongueur()