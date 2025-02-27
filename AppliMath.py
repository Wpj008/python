#fonction pair impair

def pair(a):
    if a % 2 == 0:
        print(a, "est pair")
    else:
        print(a, "est impair")

#fonction factorielle

def factorielle(a):
    b = 1
    for i in range(1, a + 1):
        b *= i
    print(f"Factorielle de {a} = {b}")

#focntion multiplication

def multiplication(a):
    for i in range(1, 11):
        print(f"{i} * {a} = {i * a}")

#fonction palindrome

def palindrome(a):
    nombre = a
    inverse = 0
    while a > 0:
        b = a % 10
        inverse = inverse * 10 + b
        a = a // 10
    if nombre == inverse:
        print(f"{nombre} est un palindrome")
    else:
        print(f"{nombre} n'est pas un palindrome")

#fonction nombre premier

def premier(n):
    if n <= 1:
        print(f"{n} n'est pas un nombre premier")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} n'est pas un nombre premier")
            return
    print(f"{n} est un nombre premier")

#fonction nombre parfait

def parfait(a):
    somme = sum(i for i in range(1, a // 2 + 1) if a % i == 0)
    if somme == a:
        print(f"{a} est un nombre parfait")
    else:
        print(f"{a} n'est pas un nombre parfait")

#fonction afficher menu

def afficheMenu():
    print("\nMENU PRINCIPAL")
    print("==============")
    print("1. Nombre pair et impair")
    print("2. Calcul de la factorielle")
    print("3. Table de Multiplication")
    print("4. Palindrome")
    print("5. Nombre Premier")
    print("6. Nombre Parfait")
    print("7. Quitter")

#fonction afficher decision

def afficheDecision():
    print("\nMenu secondaire")
    print("1. Répéter la même opération avec un nouveau nombre")
    print("2. Retourner au menu principal")


while True:
    afficheMenu()
    try:
        choix = int(input("Choisir une option (1-7) : "))
    except ValueError:
        print("Choix invalide. Entrez un chiffre entre 1 et 7.")
        continue

    if choix == 7:
        print("Merci pour votre visite !")
        break
    if choix not in range(1, 7):
        print("Option invalide. Veuillez réessayer.")
        continue

    while True:
        try:
            nombre = int(input("Entrez un nombre : "))
        except ValueError:
            print("Nombre invalide. Essayez encore.")
            continue

        match choix:
            case 1: pair(nombre)
            case 2: factorielle(nombre)
            case 3: multiplication(nombre)
            case 4: palindrome(nombre)
            case 5: premier(nombre)
            case 6: parfait(nombre)

        while True:
            afficheDecision()
            try:
                decision = int(input("Choisir une option (1-2) : "))
                if decision == 1:
                    break  # Redemande un nouveau nombre
                elif decision == 2:
                    break  # Retourne au menu principal
                else:
                    print("Option invalide. Veuillez choisir 1 ou 2.")
            except ValueError:
                print("Erreur : veuillez choisir un nombre valide.")
        if decision == 2:
            break

   
