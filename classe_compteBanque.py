class Banque:

    def __init__ (self, nom, solde):
        self.nom = nom 
        self.solde = solde 

    def depot(self):

        somme = int(input("Vous voulez effectuer un depot de combien : "))

        self.solde = somme + self.solde 

        print(f"Apres depot de {somme} $, nouveau solde {self.solde} $")

    def retrait(self):
           
         difference = int(input("Vous voulez effectuer un retrait de combien : "))

         self.solde = self.solde - difference 

         print(f"Apres retrait de {difference} $, nouveau solde {self.solde} $")

    def __repr__(self): 

        return f"Le compte de {self.nom} a un solde de {self.solde} $"


saisie1 = input("Saisir le nom du client : ")
saisie2 = int(input("Solde disponible : "))

Personne = Banque(saisie1, saisie2)

Personne.depot()

Personne.retrait()

print(Personne)