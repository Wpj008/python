class Video:
    def __init__(self, titre_video, duree_min, categorie_video):
        self.titre_video = titre_video
        self.duree_min = duree_min
        self.categorie_video = categorie_video

    def regarder_video(self):
        print("Lancement de la video...")
        print(f"La video que vous regardez est intitulée {self.titre_video}, catégorie {self.categorie_video} et dure {self.duree_min} minutes.")

    def stop_video(self):
        print("Arrêt de la video.")


class Audio:
    def __init__(self, titre_audio, nom_artiste):
        self.titre_audio = titre_audio
        self.nom_artiste = nom_artiste

    def ecouter_audio(self):
        print("Lancement de l'audio...")
        print(f"L'audio que vous écoutez est intitulé {self.titre_audio}, produit par l'artiste {self.nom_artiste}.")

    def stop_audio(self):
        print("Arrêt de l'audio.")


class Media(Video, Audio):
    def __init__(self, titre_video, categorie_video, duree_min, titre_audio, nom_artiste):
        Video.__init__(self, titre_video, duree_min, categorie_video)
        Audio.__init__(self, titre_audio, nom_artiste)


# Saisie utilisateur
saisie1 = input("Saisir le titre de la video : ")
saisie2 = input("La categorie de la video : ")
saisie3 = int(input("La durée de la video (en minutes) : "))
saisie4 = input("Saisir le titre de l'audio : ")
saisie5 = input("Saisir le nom de l'artiste : ")

# Création d'une instance de Media
Perso1 = Media(saisie1, saisie2, saisie3, saisie4, saisie5)

# Appels des méthodes
Perso1.regarder_video()
Perso1.stop_video()
Perso1.ecouter_audio()
Perso1.stop_audio()
