class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
    def get_longueur(self):
        return self._longueur
    def set_longueur(self, longueur):
        self._longueur = longueur
    def get_largeur(self):
        return self._largeur
    def set_largeur(self, largeur):
        self._largeur = largeur
    def perimetre(self):
        return 2 * (self._longueur + self._largeur)
    def surface(self):
        return self._longueur * self._largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur
    def get_hauteur(self):
        return self._hauteur

    def set_hauteur(self, hauteur):
        self._hauteur = hauteur

    def volume(self):
        return self._longueur * self._largeur * self._hauteur
rectangle1 = Rectangle(5, 10)
print("Périmètre du rectangle :", rectangle1.perimetre())
print("Surface du rectangle :", rectangle1.surface())
rectangle1.set_longueur(8)
rectangle1.set_largeur(12)
print("Nouveau périmètre du rectangle :", rectangle1.perimetre())
print("Nouvelle surface du rectangle :", rectangle1.surface())
parallelepipede1 = Parallelepipede(5, 10, 3)
print("Volume du parallélépipède :", parallelepipede1.volume())
