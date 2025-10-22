def presenceVoyelle(L):

    voyelle = ["a","e","u","i","o","y"]

    for voy in voyelle:

        if voy in L:

            print("Le mot contient au moins une voyelle.")
            return True  # Dès qu'on trouve une voyelle, on arrête et retourne True

    print("Il n'y a pas de voyelle dans le mot.")  
    return False 

List=input("saisir un mot : ")

re = presenceVoyelle(List)
