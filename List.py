def saisir():
    saisies = input("Entrez les valeurs (tapez 'fin' pour terminer) : ")

    valeurs = [valeur.strip() for valeur in saisies.split(',')]
    if 'fin' in valeurs:
        valeurs = valeurs[:valeurs.index('fin')]
        return valeurs
    
valu = saisir()

print("Les valeurs saisies sont : ", valu)