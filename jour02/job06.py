import time
import random

class Commande():
    def __init__(self):
        self.__numéro_de_commande = random.randint(1, 50)
        self.__liste_plat_commandé = []
        self.__statues_commande = ["Annulé","Commandé","En cours"]
        self.__prix = []
    def ajouter_plat_et_prix(self, new_plat, new_prix):
        if isinstance(new_plat, (str)) and isinstance(new_prix, (int)):
            self.__liste_plat_commandé.append(new_plat)
            self.__prix.append(new_prix)
        else:
            print("Le type n'est pas le bon")
    def get_num_commande(self):
        return self.__numéro_de_commande
    def get_liste_plat_commandé(self):
        return self.__liste_plat_commandé
    def annuler_une_commande(self):
        self.__statues_commande = self.__statues_commande[0]
    def commandé(self):
        for état in self.__statues_commande[1:]:
            print(f"La commande est maintenant {état}")
            self.__statues_commande = état
            time.sleep(5)
    def get_price(self):
        return sum(self.__prix)
    def get_tva(self):
        tva = self.get_price() * ( 20 / 100)
        return tva
    def get_total(self):
        return sum(self.__prix) + self.get_tva()
    
n = Commande()
print(f"Numéro de commande : {n.get_num_commande()}")
n.ajouter_plat_et_prix("Pizza",15)
n.ajouter_plat_et_prix("Tiramusu",20)
print(f"Liste commande {n.get_liste_plat_commandé()}")
n.commandé()
print(f"Prix : {n.get_price()}")
print(f"Montant tva : {n.get_tva()}")
print(f"Total : {n.get_total()}")