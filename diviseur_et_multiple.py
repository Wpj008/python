def diviseurMult(n,a,nbrSeuil):
    result = []

    for nbr in range(nbrSeuil+1):

        if nbr % n == 0 and nbr % a != 0:
            result.append(nbr)

    return result



re = diviseurMult(11,3,85)

print(re)