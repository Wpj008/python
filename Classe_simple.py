class Biscuit:
    def __init__(self,nom,forme):

        self.nom = nom
        self.forme = forme

    def cuir(self):
        print(f"Le biscuit {self.nom} a été cuit sous forme d'un {self.forme}. Bonne digestion")


saisie1 = input("Saisir le nom du biscuit : ")
saisie2 = input("Saisir la forme du biscuit : ")

biscuit = Biscuit(saisie1, saisie2)
print(biscuit.nom)
print(biscuit.forme)

biscuit.cuir()
        