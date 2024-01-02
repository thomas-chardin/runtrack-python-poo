class Point():
    def __init__(self, x=0 , y=0):
        self.x = x
        self.y = y
    def afficherX(self):
        print(self.x)
    def afficherY(self):
        print(self.y)
    def changerX(self, x):
        self.x = x
    def changerY(self, y):
        self.y = y
    def afficherLesPoints(self):
        print(f"les coordonnées du points sont {self.x} et {self.y}")
point = Point( 10, 4)
point.afficherX()
point.changerY(8)
point.afficherY()
point.changerX(2)
point.afficherLesPoints()
