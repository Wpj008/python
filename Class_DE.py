import random

class DE:

   
    def __init__(self, resultat = 0):

        self.resultat = resultat


    def lancer_un_de(self):


        self.resultat = random.randint(1, 6)

        return self.resultat
    
    def affichage(self):

        print(f"Le point obtenu est de {self.resultat}")

lancement = DE()
lancement.lancer_un_de()
lancement.affichage()
        