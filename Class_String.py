class MachainePerso:

    def __init__(self, variable_str):

        self.variable_str = variable_str

    def __add__(self, chaine):

        return self.variable_str + "|" + chaine.variable_str


    def __mul__(self, scalaire):

        return self.variable_str * scalaire
    
    def __len__(self):


        caractere_supp = [",","?","!"," ","."]
        variable_str_1 = self.variable_str

        for c in caractere_supp:
            variable_str_1 = variable_str_1.replace(c,"")

        return len(variable_str_1)
    
    def __str__(self):

        return self.variable_str
    
    def __contains__(self, sousChaine):


        if sousChaine in self.variable_str:

            return True
        
        return False
    



chaine_1 = MachainePerso("Bonjour, comment allez-vous ?")
chaine_2 = MachainePerso("Bienvenue à ce cours.")

print("Chaine_1 = ", chaine_1)
print("chaine_2 = ", chaine_2)
print("La concaténation de chaine_1 et chaine_2 donne : ", chaine_1 + chaine_2)
print("La longueur de la chaine_1 est : ", len(chaine_1))
print("La longueur de la chaine_2 est : ", len(chaine_2))