def positionElement(L,x):

    indice = []

    for i, e  in enumerate(L):

      if e == x:
        indice.append(i)

    if indice == []:
       print(f"l'element {x} ne se trouve pas dans la liste {L}")

    else: 

       return indice   


saisie = input("saisir les elements de la liste en les separants par des virgules :  ") 

L = saisie.split(",")

valeur = input("saisir la valeur à rechercher : ")

positionElement(L,valeur)

print(f" Dans la liste {L} la valeur {valeur} est à la position {positionElement(L,valeur)}")
