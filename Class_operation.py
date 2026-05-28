class Operation:

    def __init__(self, x, y):
        
        self.x = x 
        self.y = y 

    def addition(self):

        result = self.x + self.y 

        print(f"{self.x} + {self.y} = {result}")

    def soustraction(self):

        result = self.x - self.y 

        print(f"{self.x} - {self.y} = {result}")

    def multiplication(self):

        result = self.x * self.y 

        print(f"{self.x} * {self.y} = {result}")

    def division(self):

        if self.y > 0 :

         result = self.x / self.y 
         print(f"{self.x} / {self.y} = {result}")
        
        else:
            print("Division de X par Y imppossible")


saisie1 = int(input("Saisir le premier nombre : "))
saisie2 = int(input("Saisir le deuxieme nombre : "))

nombre = Operation(saisie1, saisie2)

nombre.addition()
nombre.soustraction()
nombre.multiplication()
nombre.division()
    