class TravailleurEntreprise:

    def __init__(self, nom_travailleur, salaire, age):

        self.nom_travailleur = nom_travailleur
        self.salaire = salaire
        self.age = age

    
    def afficher_info(self):

        print("Nom : ", self.nom_travailleur)
        print("Salaire : ", self.salaire)
        print("Age : ", self.age)



class Directeur(TravailleurEntreprise):

    def __init__(self, nom_directeur, salaire, age, prime):
        
        super().__init__(nom_directeur, salaire, age)

        self.prime = prime 

    def afficher_fonction(self):

        print("je suis un directeur d'entreprise ")


    def afficher_info(self):
        
        super().afficher_info()
        print(f"La prime annuelle perçue est de {self.prime} euros.")


class Ingenieur(TravailleurEntreprise):

    def __init__(self, nom_ingenieur, salaire, age, specialite):

        super().__init__(nom_ingenieur, salaire, age)
        self.specialite = specialite

    def afficher_fonction(self):

        print("Je suis un ingénieur")

    def afficher_info(self):
        
         super().afficher_info()

         print(f"Je suis un ingénieur spécialisé en {self.specialite}")



directeur = Directeur("Jules", 75000, 43, 5000)
ingenieur = Ingenieur("Jean", 40000, 32, "Intelligence Artificielle")


travailleurs = [directeur, ingenieur]

for travailleur in travailleurs:
    travailleur.afficher_fonction()
    travailleur.afficher_info()

    print()