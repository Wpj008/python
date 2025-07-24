import math
class Cercle:

    def __init__(self, x,y,R):
        
        self.x = x
        self.y = y 
        self.R = R 

    def surface(self):

        air = math.pi * self.R**2

        print(f"La surface du cercle dont le centre se situe aux coordonnées ({self.x},{self.y}) vaut : {air} ")

    def perimetre(self):

        per = 2 * math.pi * self.R

        print(f"Le périmètre du cercle dont le centre se situe aux coordonnées ({self.x},{self.y}) vaut : {per} ")


saisie1 = int(input("Saisir la coordonée de l'axe X : "))
saisie2 = int(input("Saisir la coordonée de l'axe Y : "))
saisie3 = int(input("Saisir le Rayon du : "))

cercle1 = Cercle(saisie1, saisie2, saisie3)

cercle1.perimetre()
cercle1.surface()


saisie4 = int(input("Saisir la coordonée de l'axe X : "))
saisie5 = int(input("Saisir la coordonée de l'axe Y : "))
saisie6 = int(input("Saisir le Rayon : "))

cercle2 = Cercle(saisie4, saisie5, saisie6)

cercle2.perimetre()
cercle2.surface()