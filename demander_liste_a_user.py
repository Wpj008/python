L = []

element = int(input("Entrez le nombre d'élément de la liste : "))

for i in range(element):
    valeur = int(input(f"Entrez l'element à la position {i} de la liste : "))

    L.append(valeur)


print(L)