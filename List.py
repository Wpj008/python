def menu():
    reponse = input("voulez vous saisir une autre liste ? OUI / NON : ")

    if reponse == 'oui' or reponse == 'OUI':

       saisie = input("Entrez les elements de la liste separés par des virgules : ")

       La = saisie.split(",")
       unionList(La)

    else: 

        return 0 


def unionList(L1):

    L = L1 
# la structure list(set(nom de la liste)) permet de supprimer les doublons
    L4 = list(set(L))
#la fonction sorted permet que la liste soit trier en ordre
    LF = sorted(L4)

    print(f'Liste après tri :{LF}')

    menu()

saisie = input("Entrez les elements de la liste separés par des virgules : ")

Lo = saisie.split(",")
print(Lo)

unionList(Lo)