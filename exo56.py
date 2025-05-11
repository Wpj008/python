def filtreMot():

 phrase = input("Saisir une phrase, en separant les mots avec un espace pas de virgule ou autre de ponstuation : ")
 taille = int(input("Saisir la taille minimale de sortie : "))

 mots = phrase.split()
 
 mot_filtre = []

 for mot in mots:
  
  if len(mot) >= taille:

   mot_filtre.append(mot)

#join() nous permet de reconstituer la phrase avec les mots setrouvant la la list mot_filtre
 print( " ".join(mot_filtre))
 


filtreMot()