class Employe:

    def __init__(self, nom, age):
        self.nom = nom 
        self.age = age 

    def __del__(self):

        print(f"L'employé {self.nom} agé de {self.age} ans a été supprimé par le destructeur ! ")

    def __str__(self):

        return f" L'employé  nommé {self.nom} et agé de {self.age} ans a été créé"


saisie1 = input("Saisir le nom de l'employé : ")
saisie2 = int(input("Saisir l'age de l'employé : "))

perso = Employe(saisie1, saisie2)

print(perso)
del perso