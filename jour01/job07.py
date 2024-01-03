class Personnage():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def bas(self):
        self.y = self.y + 1
    def haut(self):
        self.y = self.y - 1
    def droite(self):
        self.x = self.x + 1
    def gauche(self):
        self.y = self.y - 1
    def position(self):
        return (self.x, self.y)
personnage = Personnage()
personnage.position()
    