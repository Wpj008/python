import os

def nombreFichier(cheminDossier):
    # Liste tout le contenu du dossier
    contenu = os.listdir(cheminDossier)
    compteur = 0

    # Parcours chaque élément du dossier
    for element in contenu:
        # Construit le chemin complet de l'élément
        cheminComplet = os.path.join(cheminDossier, element)

        # Vérifie si c'est un fichier (et non un dossier)
        if os.path.isfile(cheminComplet):
            compteur += 1

    return compteur


dossier  = input("Saisir le chemin du fichier : ")
print(f"Nombre de fichiers dans le dossier {dossier} :", nombreFichier(dossier))
