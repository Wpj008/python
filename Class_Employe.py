class Employe:

    def __init__(self, nom, fonction, salaire):

        self.nom = nom 
        self.fonction = fonction
        self.salaire = salaire

    def travailler(self, nombre_heure = 0):

        self.nombre_heure = nombre_heure 

        print(f"Le salarié {self.nom} a travaillé pendant {self.nombre_heure} heures")

    def info_salaire(self):
        
        print(f"Le salarié {self.nom} a un salaire de {self.salaire} $")

    def donner_augmentation(self, somme):

        self.somme = somme

        self.somme = self.salaire + somme

        print(f"Le salarié {self.nom} a obtenu une augmentation de {somme}, son salire est desormais à {self.somme}")

    def info_fonction(self):

        print(f"Le salarié {self.nom} occupe une fonction de {self.fonction}")



saisie1 = input("Nom de l'employé : ")
saisie2 = input(f"Fonction de {saisie1}: ")
saisie3 = int(input(f"Salaire de {saisie1} : "))

agent1 = Employe(saisie1, saisie2, saisie3)

agent1.info_fonction()
nombre = int(input("Nombre d'heure de travail : "))
agent1.travailler(nombre)
somme = int(input("Montant de l'augmentation : "))
agent1.donner_augmentation(somme)
agent1.info_salaire()

saisie4 = input("Nom de l'employé : ")
saisie5 = input(f"Fonction de {saisie4}: ")
saisie6 = int(input(f"Salaire de {saisie4} : "))

agent2 = Employe(saisie4, saisie5, saisie6)

agent2.info_fonction()
nombre = int(input("Nombre d'heure de travail : "))
agent2.travailler(nombre)
somme = int(input("Montant de l'augmentation : "))
agent2.donner_augmentation(somme)
agent2.info_salaire()
