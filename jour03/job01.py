class Ville():
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants
    def get_nom(self):
        return self.__nom
    def get_nombre_habitants(self):
        return self.__nombre_habitants
    def set_nombre_habitants(self, nombre_habitants):
        self.__nombre_habitants = nombre_habitants          

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age
    def get_ville(self):
        return self.__ville
    def ajouter_population(self):
        ville = self.__ville
        ville.set_nombre_habitants(ville.get_nombre_habitants() + 1)

y = Ville("Marseille", 861635)
n = Ville("Paris", 1000000)
print(f"Population de la ville de Paris : {n.get_nombre_habitants()} habitants")
print(f"Population de la ville de Marseille : {y.get_nombre_habitants()} habitants")
jhon = Personne("John", 45, n)
jhon.ajouter_population()
myrthille = Personne("Myrtille", 4, n)
myrthille.ajouter_population()
chloé = Personne("Chloé", 18 ,y)
chloé.ajouter_population()
print(f"Mise a jour de la Population de la ville de Paris {n.get_nombre_habitants()} habitants")
print(f"Mise a jour de la Population de la ville de Marseille {y.get_nombre_habitants()} habitants")