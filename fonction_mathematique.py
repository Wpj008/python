# exo 34 

def fonction(a,b,x) :
    
    reponse = a * (x**3) + 2 * a *(x**2) + b

    return reponse 

print("entrez 3 valeurs : ")

nom1 = input("Valeur 1 : ")
nom2 = input("Valeur 2 : ")
nom3 = input("valeur 3 : ")

n1 = int(nom1)
n2 = int(nom2)
n3 = int(nom3)

az = fonction(n1,n2,n3)

print(az)