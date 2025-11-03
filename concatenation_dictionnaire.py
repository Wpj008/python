def cocatDict(d1, d2):
    d1.update(d2)  # Mettez à jour d1 avec les éléments de d2
    return d1  # Retourne d1 après la mise à jour

# Appel de la fonction et affichage du résultat
resultat = cocatDict({"a":[1,2,3],"b":[4,6,5]}, {"c":[7,8],"d":[9,5]})
print(resultat)  # Affiche le dictionnaire mis à jour
