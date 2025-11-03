nombre = input("Saisir un nombre : ")

somme = 0

for chiffre in nombre:

    somme = somme + int(chiffre)


    
print(f"la somme de tous les chiffres est {somme}")