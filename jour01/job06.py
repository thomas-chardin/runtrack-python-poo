class Animal():
    def __init__(self):
        self.age = 0
        self.prenom = ""
    def afficherAge(self):
        print(f"L'age de l'animal {self.age} ans")
    def viellir(self):
        self.age = self.age + 1
    def nommer(self, prenom):
        self.prenom = prenom
    def afficherNom(self):
        print(f"L'animal se nomme {self.prenom}")
animal = Animal()
animal.afficherAge()
animal.viellir()
animal.afficherAge()
animal.nommer("Luna")
animal.afficherNom()