def lireFichier(cheminFichier, mot):

  f = open(cheminFichier,"r")
  fichier = f.read()
 # mots = fichier.split()
  mots = fichier.replace(mot,"")

  f.close()


  print(mots)

saisi = input("Saisir le chemin du fichier : ")
valeur = input("Saisir le mot à supprimer dans le fichier : ")


lireFichier(saisi,valeur)
