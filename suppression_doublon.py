def supprimeDoublon(L):

    for i in L:

        a = L.count(i)

        if a >= 2:

            for b in range(a-1):

                L.remove(i)

        
    L.sort()

    print(f"Liste après suppression des doublons {L}")

    return L

L = [1, 2, 4, 5, 2, 3, 1, 5, 3]

supprimeDoublon(L)

