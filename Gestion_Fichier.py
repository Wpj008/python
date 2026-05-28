class ManipulationFichier:
    fichier = ""
    def __init__(self, cheminFichier):
        self.cheminFichier = cheminFichier
       
        self.fichier = open(cheminFichier, 'r+')
        #fichier.read()

        print(f"Le fichier {self.cheminFichier} est mode lecture et écriture !")


    def ecrire_fichier(self, phrase):

        self.fichier.write(phrase) 

        print(f"La phrase '{phrase}' a été écrite dans le fichier : {self.cheminFichier}")

    def __del__(self):
        
        self.fichier.close()

        print(f"Le fichier {self.cheminFichier} a été fermé.")



saisie1 = input("Saisir le chemin du fichier : ")
Perso = ManipulationFichier(saisie1)
saisie2 = input("Saisir le texte : ")
Perso.ecrire_fichier(saisie2)
del Perso
