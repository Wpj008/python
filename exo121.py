class Calculatrice:

    def __init__(self):
        print()

     

    def somme(self, x,y):
        self.x = x
        self.y = y

        return x + y
    def multiplication(self, x, y):
        self.x = x
        self.y = y

        return x * y
    def division(self, x, y):
        self.x = x
        self.y = y

        if(x >= y):
            return x/y
        else:
            return y/x
        

saisie1 = int(input("Saiisir le premier nombre : "))
saisie2 = int(input("Saisir le deuxieme nombre : "))

result1 = Calculatrice(saisie1, saisie2)
result1.somme()

result2 = Calculatrice(saisie1, saisie2)
result2.multiplication()

result3 = Calculatrice(saisie1, saisie2)
result3.division()

print(f" {saisie1} + {saisie2} = {result1}")
print(f" {saisie1} x {saisie2} = {result2}")
print(f" {saisie1} : {saisie2} = {result3}")

