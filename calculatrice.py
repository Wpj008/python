def addition(a,b):

    somme = a + b

    return somme

def soustraction(a,b):

    difference = a - b

    return difference

def multiplication(a,b):

    produit = a * b

    return produit

def division(a,b):

    if b != 0 :

        quotient = a / b

    else : 

        print("Impossible d'effectuer la division")

    return quotient

def afficheMenu():

    print("Menu Principal")
    print("==============")

    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    
def afficheDecision():
    print("1. Répeter l'opération")
    print("2. Revenir au Menu")

    
while True:  # Boucle principale
    afficheMenu()

    try:
        choix = int(input("Choisissez une option (1-5) : "))
    except ValueError:
        print("Choix invalide. Entrez un chiffre entre 1 et 5.")
        continue  # Retour au menu si erreur

    if choix == 5:
        print("Merci pour votre visite !")
        break  # Quitter la boucle

    if choix not in [1, 2, 3, 4]:
        print("Option invalide. Veuillez réessayer.")
        continue

    try:
        nombre1 = float(input("Saisir la première valeur : "))
        nombre2 = float(input("Saisir la deuxième valeur : "))
    except ValueError:
        print("Nombre invalide. Essayez encore.")
        continue

    match choix:
        case 1:
            resultat = addition(nombre1, nombre2)
            print(f"{nombre1} + {nombre2} = {resultat}")

        case 2:
            resultat = soustraction(nombre1, nombre2)
            print(f"{nombre1} - {nombre2} = {resultat}")

        case 3:
            resultat = multiplication(nombre1, nombre2)
            print(f"{nombre1} * {nombre2} = {resultat}")

        case 4:
            resultat = division(nombre1, nombre2)
            if resultat is not None:
                print(f"{nombre1} / {nombre2} = {resultat}")

    while True:  # Boucle pour répéter ou revenir au menu
        afficheDecision()
        try:
            decision = int(input("Choisissez une option (1-2) : "))
            if decision == 1:
                break  # Refaire la même opération
            elif decision == 2:
                break  # Retour au menu principal
            else:
                print("Option invalide. Veuillez choisir 1 ou 2.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")