class Animal:

    def __init__(self, nom_animal):

        self.nom_animal = nom_animal

    def parler(self):

        pass

class Chat(Animal):

    def __init__(self, nom_chat):

        super().__init__(nom_chat)

    def parler(self):


        return self.nom_animal + " Dis Meooowww Meooowwww"
    

class Chien(Animal):

    def __init__(self, nom_chien):

        super().__init__(nom_chien)

    def parler(self):

        return self.nom_animal + " Dis woooff woooofff"
    

loulou = Chien("loulou")
lolo = Chat("lolo")

print(loulou.parler())
print(lolo.parler())