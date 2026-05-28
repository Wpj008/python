class Personne:

    def __init__(self, nom, age, sexe):

        self.nom = nom 
        self.age = age 
        self.sexe = sexe 

    def presenter(self):

        print(f"Mon nom est {self.nom}, j'ai {self.age} ans et je suis de sexe {self.sexe}")

    def estAdulte(self):

        if self.age >= 18 :
            print(True)
             
        else:
            print(False)
        
        
saisie1 = input("Saisir votre nom : ")
saisie2 = int(input("Saisir votre age : "))
saisie3 = input("Votre sexe (M/F) : ")

personne = Personne(saisie1, saisie2, saisie3)

personne.presenter()
personne.estAdulte()