class Vehicule:

    def __init__(self, marque, vitesse = 0):

        self.marque = marque 
        self.vitesse = vitesse

    def acceleration(self, VA):

        self.VA = VA

        self.VA = VA + self.vitesse

        print(f"Vitesse apres acceleration : {self.VA} km/h")

    def deceleration(self, VD):

        self.VD = VD

        VD = self.VA - VD

        print(f"Vitesse après reduction : {VD} km/h")

    def afficher(self):

        print(f"Vitesse Initiale : {self.vitesse} km/h")

class Voiture(Vehicule):

    def __init__(self, marque, vitesse, klaxon = "tuuuut"):

     super().__init__(marque, vitesse)

     self.klaxon = klaxon 

    def klaxonner(self):

        print(self.klaxon)


saisie1 = input("Saisir la marque de la voiture : ")
saisie2 = int(input("Quelle est la vitesse initiale : "))

VA = int(input("Vitesse A: "))
voiture = Voiture(saisie1, saisie2)

voiture.acceleration(VA)

VD = int(input("Vitesse D: "))

voiture.deceleration(VD)
voiture.klaxonner()
voiture.afficher()