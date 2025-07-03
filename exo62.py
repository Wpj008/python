def lireFichier(cheminFichier, mot):

  f = open(cheminFichier,"r")
  fichier = f.read()
  mots = fichier.split()
  nombre = mots.count(mot)

  f.close()


  print(nombre)

saisi = input("Saisir le chemin du fichier : ")
valeur = input("Saisir le mot à rechercher dans le fichier : ")


lireFichier(saisi,valeur)
