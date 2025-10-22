def lireFichier(cheminFichier):

  f = open(cheminFichier,"r")
  fichier = f.read()

  f.close()


  print(fichier)

saisi = input("Saisir le chemin du fichier : ")


lireFichier(saisi)