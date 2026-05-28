class Ordinateur:
    def __init__(self, marque, modele, prix):

        self.marque = marque
        self.modele = modele
        self.prix = prix

    def listing_marques(self):

        print("Dell, HP, Lenovo et Apple") 

class OrdinateurBureau(Ordinateur): 

    def __init__(self, marqueDesk, modeleDesk, prixDesk, taille_UC):

        super().__init__(marqueDesk, modeleDesk, prixDesk)
       
        self.taille_UC = taille_UC

    def afficher_information(self):

        print(f"L'ordinateur de Bureau de marque {self.marque}, modèle {self.modele} ayant une Unité centrale de {self.taille_UC} cm vaut {self.prix} €")


class OrdinateurPortable(Ordinateur):

    def __init__(self, marquePC, modelePC, prixPC, taillePC):

        super().__init__(marquePC, modelePC, prixPC)
    
        self.taillePC = taillePC


    def afficher_infirmations(self):

        print(f"L'ordianteur portable de marque {self.marque}, modèle {self.modele} ayant une de {self.taillePC} pousse coûte {self.prix} €")



PC1 = OrdinateurBureau("HP", "HP core i5", 560, 8)
PC2 = OrdinateurPortable("Dell", "7145", 550, 15)

PC1.afficher_information()
PC2.afficher_infirmations()

