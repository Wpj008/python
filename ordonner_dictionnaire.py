def ordonnerDict(d):
    # Convertir les éléments du dictionnaire en liste de tuples
    Liste_tuple = list(d.items())
    
    # Trier la liste par clé (clé = x[0])
    Liste_tuple.sort(key=lambda x: x[0])
    
    # Reconvertir en dictionnaire
    return dict(Liste_tuple)

# Test
print(ordonnerDict({8: 9, 2: 3, 7: 6}))
