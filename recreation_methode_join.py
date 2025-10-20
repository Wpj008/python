def Fonction_join(L, caractere):

    chaine_caractere = ""

    for i in range(len(L)):

        chaine_caractere = chaine_caractere + L[i]

        if i < len(L) - 1:

            chaine_caractere = chaine_caractere + caractere

    return chaine_caractere

saisie = input("saisir les mots de la liste en espaçant : ")

L1 = saisie.split(" ")

print(Fonction_join(L1, ", "))

