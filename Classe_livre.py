class Livre:

    def __init__(self,titre, auteur, prix):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix

    def afficher_info(self):

        print(f"Le Livre intitulé '{self.titre}', écrit par {self.auteur} se vend à {self.prix} $")

saisie1 = input("Saisir le nom du livre : ")
saisie2 = input("Saisir le nom de l'auteur : ")
saisie3 = input("Saisir le prix du livre : ")

livre = Livre(saisie1, saisie2, saisie3)

livre.afficher_info()
