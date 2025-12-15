class Voiture: 

    def __init__(self, marque, couleur, nomConducteur, KmDebut):
        self.marque = marque 
        self.couleur = couleur 
        self.nomConducteur = nomConducteur
        self.kmDebut = KmDebut 

    def choixConducteur(self):

        conducteur = input("Qui est le conducteur que vous voulez : ")

        return conducteur

    def distance(self):

        km = int(input("Distance parcourue : "))

        km = km + self.kmDebut

        return km

    def afficher(self):

        print(f" La voiture de marque {self.marque} de couleur {self.couleur} dont le conducteur est {self.choixConducteur()} possède un kilometrage de {self.distance()} km")


saisie1 = input("Marque de la voiture : ")
saisie2 = input("Couleur de la voiture : ")
saisie3 = input("Nom du conducteur : ")
saisie4 = int(input("Kilomètrage au depart : "))

Perso = Voiture(saisie1, saisie2, saisie3, saisie4)

Perso.afficher()
