class Student():
    def __init__(self, nom, prenom,numéro_étudiant):
        self.nom = nom
        self.prenom = prenom
        self.numéro_étudiant = numéro_étudiant
        self.nombre_crédit = 0
        self.eval = self.__studentEval()
    def add_crédits (self,crédit_plus):
        if crédit_plus > 0:
            self.nombre_crédit += crédit_plus
            self.eval = self.__studentEval()
    def __studentEval(self):
        if self.nombre_crédit >= 90:
            return "Excellent"  
        elif self.nombre_crédit >= 80:
            return "Très bien"
        elif self.nombre_crédit >= 70:
            return "Bien"
        elif self.nombre_crédit >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    def studentInfo(self):
        print(f"Nom = {self.nom}")
        print(f"Prénom = {self.prenom}")
        print(f"Id = {self.numéro_étudiant}")
        print(f"Niveau = {self.eval}")

n = Student("Tansel", "Edine", 270)
n.add_crédits(20)
n.add_crédits(40)
n.studentInfo()



        


