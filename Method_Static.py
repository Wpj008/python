class Calculatrice:

    def __init__(self, x, y):
        self.x = x
        self.y = y

     

    def somme(self):
        

        return self.x + self.y
    def multiplication(self):
     

        return self.x * self.y
    def division(self):
      
        if(self.x >= self.y):
            return self.x/self.y
        else:
            return self.y/self.x
        

saisie1 = int(input("Saiisir le premier nombre : "))
saisie2 = int(input("Saisir le deuxieme nombre : "))

calc = Calculatrice(saisie1, saisie2)
result1 = calc.somme()


result2 = calc.multiplication()


result3 = calc.division()

print(f" {saisie1} + {saisie2} = {result1}")
print(f" {saisie1} x {saisie2} = {result2}")
print(f" {saisie1} : {saisie2} = {result3}")

