class NombreComplexe:

    def __init__(self, reel, img):
        self.reel = reel 
        self.img = img 

#surchage de la representation
    def __str__(self):
        return str(self.reel) + " + " + str(self.img) + "i"
    
    def __repr__(self):
        return str(self.reel) + " + " + str(self.img) + "i"
    

nbr_reel = int(input("Saisir le nombre réel : "))
nbr_img = int(input("Saisir le nombre imaginaire sans le 'i' : "))

nbr1 = NombreComplexe(nbr_reel, nbr_img)

print(nbr1)

