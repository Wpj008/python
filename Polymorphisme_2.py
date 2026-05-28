class Texte:

    def __init__(self, phrase):

        self.phrase = phrase

    def afficher_texte(self):

        print(self.phrase)


class TexteItalique(Texte):

    def __init__(self, phrase):

        super().__init__(phrase)

    def afficher_texte(self):
        
        print("_" + self.phrase + "_")


class TexteBold(Texte):

    def __init__(self, phrase):

        super().__init__(phrase)

    def afficher_texte(self):
        
        
        print("**" + self.phrase + "**")



texte_1 = Texte("Apprendre la POO en Python")
texte_2 = TexteItalique("Apprendre la POO en Python")
texte_3 = TexteBold("Apprendre la POO en Python")

textes = [texte_1, texte_2, texte_3]


for texte in textes:

    texte.afficher_texte()