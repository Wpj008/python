class Carte:

    def __init__(self, rang, symbole):

        self.rang = rang 
        self.symbole = symbole 
    def __eq__(self, carte):

        if carte.rang == self.rang and carte.symbole == self.symbole:
            return True 
        return False
    
    def __lt__(self, carte):

        if self.rang == carte.rang:
            return self.symbole < carte.symbole 
        return self.rang < carte.rang
    
    def __str__(self):

        return f"La carte est de rang {self.rang} et de symbole {self.symbole}"


enseignes = [chr(9824), chr(9825), chr(9826), chr(9827)]
rangs = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14,}

trefle_1, rangs_1 = enseignes[3], rangs["8"]
coeur_2, rangs_2 = enseignes[1], rangs["3"]
pique_3, rangs_3 = enseignes[0], rangs["8"]

carte_1 = Carte(rangs_1, trefle_1)
carte_2 = Carte(rangs_2, coeur_2)
carte_3 = Carte(rangs_3, pique_3)

print(carte_1)
print(carte_2)
print(carte_3)

print(carte_1 > carte_2)
print(carte_1 == carte_3)