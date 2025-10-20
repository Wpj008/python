def SommeSeq(L,i,j):
    Lij = L[i:j+1]
    return sum(Lij)

def PlusGrandeSomme(L):

    somme_max = L[0]

    for i in range(len(L)):

        for j in range(i, len(L)):

            s = SommeSeq(L, i, j)

            if s > somme_max:

                seq = L[i:j+1]

                somme_max = s

                return somme_max, seq
            


print(PlusGrandeSomme([-6,1,8,-7,1,9,-1,2]))