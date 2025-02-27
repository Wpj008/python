def moyenne(L):

    a = 0
    somme = 0

    for b in L:

        a = a + 1
        somme = somme + b

    c = somme / a

    print(f"La moyenne est de {c}")

L = [1,2,4,5]

moyenne(L)


