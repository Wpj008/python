def presenceNombre(cheminFichier):
   
    f = open(cheminFichier, "r")
    contenu = f.read()
    f.close()

    
    for caractere in contenu:
        if caractere.isdigit():
            return True  
    return False



chemin = input("Saisir le chemin du fichier : ")

resultat = presenceNombre(chemin)
print(resultat)
