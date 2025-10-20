class Point2D:

    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def __add__(self, p):
        return Point2D(self.x + p.x, self.y + p.y)#surcharge de l'operateur +
    
    def __sub__(self, p):
        return Point2D(self.x - p.x, self.y - p.y)#surcharge de l'operateur -
    
    def __mul__(self, p):
        return Point2D(self.x * p.x, self.y * p.y)#surcharge de l'operateur *
    
    def __truediv__(self, p):
        return(self.x / p.x, self.y / p.y)#surcharge de l'operateur /
    
    def __str__(self):
        return f"( {self.x}, {self.y})"
    
L = []

for i in range(1, 5):
        L.append(int(input((f"Saisir la coordonnée à la place {i} : "))))

print(" Coordonnées saisies :", L)

# Création des vecteurs
point1 = Point2D(L[0], L[1])
point2= Point2D(L[2], L[3])

print("La somme des points :", point1 + point2)

print("La difference des points :", point1 - point2)

print("Le produit des points :", point1 * point2)
print(" Division des points :", point1 / point2)


