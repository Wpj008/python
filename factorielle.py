def calculfacto(n):

    b = 1

    for c in range(n,0,-1):

        b = b * c

    print(b)

    return b


L = int(input("saisir un nombre : "))

calculfacto(L)