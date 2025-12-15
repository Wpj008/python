import string
import random 

#creation d une liste de caractere à partir de laquelle nous allons generer notre mdp aleatoire
Liste_carctere = list(string.ascii_letters + string.digits + "!*%$#@&")

def genereMdp(caracteres, taille):

    random.shuffle(caracteres) #melange aleatoire des caracteres

    mdp = [] #creation de la liste qui va contenir le mdp 

    for i in range(taille): 
        aleatoire = random.choice(caracteres) #choisi aleatoirement un caractere jusqu'à atteindre la taille voulu puis 
                                              

        mdp.append(aleatoire) # ajouter dans la liste mdp


    random.shuffle(mdp) #melanger une seconde fois la liste

    mdp = "".join(mdp) # convertir la liste en chaine de caractere 

    print(mdp)
    
saisi = int(input("saisir la taille du mdp : "))
    
genereMdp(Liste_carctere, saisi)