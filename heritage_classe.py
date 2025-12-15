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


class parallelepipede:

    def __init__(self, hauteur, largeur, longueur):
            
            Rectangle().__init__(self, largeur, longueur)

            self.hauteur = hauteur

    def volume(self):
         
         valeur = (self.largeur * self.longueur) * self.hauteur

         print(f"Le volume du parallelepipede de longueur {self.longueur} cm, largeur {self.largeur} cm et de hauteur {self.hauteur} cm vaut {valeur} ")

     

saisie1 = int(input("Saisir la largeur en cm : "))
saisie2 = int(input("Saisir la longueur en cm : "))
saisie3 = int(input("Saisir la longueur en cm : "))

Resultat = parallelepipede(saisie1, saisie2, saisie3)

Resultat.perimetre()
Resultat.surface()
Resultat.volume()