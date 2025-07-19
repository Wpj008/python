def nombrePair(N):

    if N == 1:

        return False
    
    return nombreImpair(N-1)

def nombreImpair(N):

    if N == 1:

        return True
    
    return nombrePair(N-1)

saisie = int(input("Saisir un nombre : "))
print(nombrePair(saisie))