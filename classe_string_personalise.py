import string

liste_carac = list(string.digits) + [",","."]
class StrPerso:

    def __init__(self, chaine):
        liste_chaine = list(chaine)

        for c in liste_chaine:
            if c in liste_carac:
                print("L'instance créée ne doit contenir que des lettres alphabetiques : ")
                print(f"Le caractere {c} sera suprimé")

                chaine = chaine.replace(c, "")

        self.chaine = chaine

    def __add__(self, nouvelle_chaine):
        if nouvelle_chaine in liste_carac:

            return f"Vous ne pouvez pas ajuster de {nouvelle_chaine} à la chaine"
        else:
            self.chaine = self.chaine + nouvelle_chaine
        return self.chaine
    def __repr__(self):
        return self.chaine
    

chaine1 = StrPerso("Bon,jour")
chaine1 + ","
chaine1 + "."
chaine2 = chaine1 + " ça va"
print(chaine2)