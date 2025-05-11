def nombreOccurrence(L):
    resultat = []
    deja_vu = []

    for e in L:
        if e not in deja_vu:
            resultat.append((e, L.count(e)))
            deja_vu.append(e)

    print(resultat)

saisie = input("saisir des elements en les separants par des virgules : ")
Liste = saisie.split(",")

nombreOccurrence(Liste)