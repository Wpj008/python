def ecrireFichier(cheminFichier, texte):

    f = open(cheminFichier, "w")

    f.write(texte)

    f.close()

chemin = input("Saisir le chemin du fichier : ")
saisie = input("Saisir le texte : ")

ecrireFichier(chemin, saisie)