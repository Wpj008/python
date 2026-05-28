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


class Etudiant(Personne): #Heritage de la class Personne par Etudiant

    def __init__(self,nom,age,sexe,niveau):
        super().__init__(nom,age,sexe) #Nous permet d'acceder aux attribur de la class mere
       
       
        self.niveau = niveau 

    def inscription(self, etudiant_inscrit):

        self.etudiant_inscrit = etudiant_inscrit

        
        etudiant_inscrit.append((self.nom,self.age ,self.sexe,self.niveau))

        

        print (f"Les etudiants inscrits aux cours sont :  {etudiant_inscrit}")



etudiant_inscrit = []

saisie1 = input("Saisir votre nom : ")
saisie2 = int(input("Saisir votre age : "))
saisie3 = input("Votre sexe (M/F) : ")
saisie4 = input("Votre niveau d'etude : ")

saisie5 = input("Saisir votre nom : ")
saisie6 = int(input("Saisir votre age : "))
saisie7 = input("Votre sexe (M/F) : ")
saisie8 = input("Votre niveau d'etude : ")


personne1 = Etudiant(saisie1, saisie2, saisie3,saisie4)

personne2 = Etudiant(saisie5, saisie6, saisie7,saisie8)

personne1.presenter()
personne1.estAdulte()
personne2.presenter()
personne2.estAdulte()
personne1.inscription(etudiant_inscrit)#affiche un seul eleve
personne2.inscription(etudiant_inscrit)#affiche les 2 eleves