def verifMaj(L):
    for lettre in L:
        if lettre.isupper():
            return True  # Dès qu'on trouve une majuscule, on retourne True
    return False  # Si aucune majuscule trouvée, retourne False

C = input("Saisir une phrase : ")

verifMaj(C)

if verifMaj(C):  # On vérifie le retour de la fonction
    print("La phrase contient au moins une majuscule.")
else:
    print("La phrase ne contient aucune majuscule.")