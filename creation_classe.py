class Personne:

    def __init__(self, poids, taille, age):
        self.taille = taille 
        self.poids = poids 
        self.age = age 
        self.resultat = None  # on l'initialise ici

    def calculIMC(self):
        self.resultat = self.poids / (self.taille ** 2)

    def interpretationIMC(self):
        if self.resultat is None:
            print("L'IMC n'a pas encore été calculé.")
            return

        if self.resultat <= 18.5:
            print("Le résultat du calcul de l'IMC indique une insuffisance pondérale.")
        elif self.resultat >= 30:
            print("La personne est obèse.")
        else:
            print("La personne est en surpoids ou a une corpulence normale.")


# ✅ Saisies utilisateur correctement récupérées
poids = int(input("Saisir votre poids (kg) : "))
taille = float(input("Saisir votre taille (m) : "))
age = int(input("Saisir votre âge : "))

#  Création de l'objet
personne = Personne(poids, taille, age)

#  Calcul et interprétation de l'IMC
personne.calculIMC()
personne.interpretationIMC()
