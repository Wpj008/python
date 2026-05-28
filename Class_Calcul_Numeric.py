class Calcul_Numerique:

    def __init__(self, nombre):
        self.nombre = nombre 

    def factorielle(self):
    
        b = 1

        for i in range(1, self.nombre + 1):

            b = b * i

        print(f"factorielle de {self.nombre} = {b}")

    def pair(self):

        if self.nombre % 2 == 0:

            print(f"{self.nombre} est un nombre pair")
        else:
            print(f"{self.nombre} n'est pas un nombre pair")

    def premier(self):
     if self.nombre <= 1:
        print(f"{self.nombre} n'est pas un nombre premier")
        return
     for i in range(2, int(self.nombre**0.5) + 1):
        if self.nombre % i == 0:
            print(f"{self.nombre} n'est pas un nombre premier")
            return
     print(f"{self.nombre} est un nombre premier")


    def diviseur(self):
     L = []
     for i in range(1, self.nombre + 1):
        if self.nombre % i == 0:
             L.append(i)
     print(f"Les diviseurs de {self.nombre} sont {L}")
             #print(f"{i} est un diviseur de {self.nombre}")

           

saisie = int(input("Saisir un nombre : "))

nombre = Calcul_Numerique(saisie)
nombre.factorielle()
nombre.diviseur()
nombre.pair()
nombre.premier()


         