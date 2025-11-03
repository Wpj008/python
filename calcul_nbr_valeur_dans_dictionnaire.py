def nbrValeurdir(d):
    d_cle = list(d.keys())  # Récupère les clés du dictionnaire
    nbr_valeur = 0  # Initialisation du compteur des valeurs

    for cle in d_cle:
        longueur_val = len(d[cle])  # Récupère le nombre d'éléments dans la liste associée à la clé
        nbr_valeur += longueur_val  # Ajoute cette longueur au compteur

    return nbr_valeur  # Retourne le total des valeurs

# Appel de la fonction et affichage du résultat
resultat = nbrValeurdir({ "jule":[15,70], "jean":[16,68], "jonas":[17,58]})
print(resultat)  # Affiche 6

