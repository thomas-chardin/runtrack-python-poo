class Personne : 
    def __init__(self, prenom, nom):
      self.prenom = prenom
      self.nom = nom 
    def SePresenter(self):
        print(f"Je suis {self.prenom} {self.nom}")
personne = Personne("John","Doe")
personne2 = Personne("Jean","Dupond")
personne.SePresenter()
personne2.SePresenter()