'''
Écris une fonction fusionListes(L1, L2) qui prend deux listes d'entiers. Elle doit :

ajouter tous les éléments de L2 à L1,

mais uniquement ceux qui ne sont pas déjà dans L1,

et ensuite trier la liste finale par ordre décroissant.
'''

def fuisonListe(L1,L2):

 L = L1 + L2

 Liste = list(set(L))

 Liste.sort(reverse = True)

 print(Liste)


saisie1 = input("saisirles elements de la première liste, en espaçant avec des virgules : ")
saisie2 = input("saisirles elements de la deuxième liste, en espaçant avec des virgules : ")

L1 = saisie1.split(",")
L2 = saisie2.split(",")

fuisonListe(L1,L2)