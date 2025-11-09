class Rectangle:

    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def perimetre(self):

        per = (self.longueur + self.largeur) * 2

        print(f"Le perimetre du rectangle de {self.longueur} cm de longueur et {self.largeur} cm de largeur vaut {per} cm")

    def surface(self):

        sur = self.largeur * self.longueur
        print(f"La surface du rectangle de {self.longueur} cm de longueur et {self.largeur} cm de largeur vaut {sur} cm²")


saisie1 = int(input("Saisir la largeur en cm : "))
saisie2 = int(input("Saisir la longueur en cm : "))

Resultat = Rectangle(saisie1, saisie2)

Resultat.perimetre()
Resultat.surface()