L = []

for nbr in range(100,1000):

    str_nbr = str(nbr)#convertion du nombre en chaine de caracteres

    somme_chiffre = int(str_nbr[0]) + int(str_nbr[1]) + int(str_nbr[2])#somme des chiffre du nombre

    produit_chiffre = int(str_nbr[0]) * int(str_nbr[1]) * int(str_nbr[2])#produit des chiffres du nombre

    if produit_chiffre % somme_chiffre == 0:

        L.append(nbr)

print(L)

