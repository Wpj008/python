def cleMaxValeur(d):
    cle_val = []

    dict_cle = list(d.keys())

    for cle in dict_cle:
        nombre_valeur = len(set(d[cle]))
        cle_val.append((cle, nombre_valeur))

    # On trie la liste des (clé, nombre de valeurs uniques) par ordre croissant
    cle_val.sort(key=lambda x: x[1])

    # On prend la clé qui a le plus grand nombre de valeurs uniques
    cle_max_valeur = cle_val[-1][0]

    return cle_max_valeur



d = {}
  
nb_cle = int(input("Combien de clés voulez-vous ajouter : "))

for i in range(nb_cle):
    cle = input(f"Saisir le nom de la clé n°{i+1} : ")
    valeurs_texte = input(f"Saisir les valeurs pour la clé '{cle}' (séparées par des virgules) : ")
    valeurs = valeurs_texte.split(",")  # transforme en liste
    d[cle] = valeurs

# Appel de la fonction et affichage du résultat
resultat = cleMaxValeur(d)
print(f"La clé qui a le plus grand nombre de valeurs uniques est : {resultat}")
