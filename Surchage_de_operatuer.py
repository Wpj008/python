class Vecteur4D:

    def __init__(self, u, v, x, y):
        self.u = u
        self.v = v 
        self.x = x 
        self.y = y 

    def __add__(self, vecteur):
        return Vecteur4D(self.u + vecteur.u, self.v + vecteur.v,
                         self.x + vecteur.x, self.y + vecteur.y)

    def __sub__(self, vecteur):
        return Vecteur4D(self.u - vecteur.u, self.v - vecteur.v,
                         self.x - vecteur.x, self.y - vecteur.y)

    def __mul__(self, vecteur):
        return Vecteur4D(self.u * vecteur.u, self.v * vecteur.v,
                         self.x * vecteur.x, self.y * vecteur.y)

    def __truediv__(self, scalaire):
        return Vecteur4D(self.u / scalaire, self.v / scalaire,
                         self.x / scalaire, self.y / scalaire)

    def __str__(self):
        return f"({self.u}, {self.v}, {self.x}, {self.y})"

L = []
for i in range(1, 9):
    L.append(int(input(f"Saisir la coordonnée à la place {i} : ")))

print(" Coordonnées saisies :", L)

# Création des vecteurs
Vecteur1 = Vecteur4D(L[0], L[1], L[2], L[3])
Vecteur2 = Vecteur4D(L[4], L[5], L[6], L[7])

print("La somme des vecteurs :", Vecteur1 + Vecteur2)

print("La difference des vecteurs :", Vecteur1 - Vecteur2)

print("Le produit des vecteurs :", Vecteur1 * Vecteur2)

scalaire = float(input(" Saisir un scalaire pour la division : "))
print(" Division du Vecteur1 :", Vecteur1 / scalaire)

scalaire = float(input(" Saisir un scalaire pour la division : "))
print(" Division du Vecteur1 :", Vecteur2 / scalaire)