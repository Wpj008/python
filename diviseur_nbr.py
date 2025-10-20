def diviseur(a):
    for b in range(a,0,-1):
        if a % b == 0:
            print(f"{b} est un diviseur de {a}")



c = int(input("saisir un nombre : "))

diviseur(c)