


print("Nous allons comparer les performances des garçons et des filles dans différentes matières.")

# Initialisation des matières avec des tableaux séparés pour chaque groupe
filles_francais = []
filles_anglais = []
filles_math = []
filles_physique = []

garcons_francais = []
garcons_anglais = []
garcons_math = []
garcons_physique = []

# Fonction pour entrer les notes
def collecter_notes(nom_matiere, groupe):
    print(f"\nEntrez les notes pour {nom_matiere}. Tapez '-1' pour arrêter.")
    while True:
        try:
            note = float(input("Note : "))
            if note <= -1:  # Arrêter la saisie
                break
            groupe.append(note)
        except ValueError:
            print("Veuillez entrer une note valide.")

# Collecte des données pour les filles
print("\n*** Notes des Filles ***")
collecter_notes("français", filles_francais)
collecter_notes("anglais", filles_anglais)
collecter_notes("mathématiques", filles_math)
collecter_notes("physique", filles_physique)

# Collecte des données pour les garçons
print("\n*** Notes des Garçons ***")
collecter_notes("français", garcons_francais)
collecter_notes("anglais", garcons_anglais)
collecter_notes("mathématiques", garcons_math)
collecter_notes("physique", garcons_physique)

# Fonction pour calculer la moyenne et les échecs
def calculer_moyenne_et_echecs(groupe):
    if len(groupe) == 0:  # Éviter la division par zéro
        return 0, 0
    moyenne = sum(groupe) / len(groupe)
    echecs = sum(1 for note in groupe if note < 10)
    return moyenne, echecs

# Affichage des résultats
def afficher_resultats(nom, francais, anglais, math, physique):
    print(f"\n*** Résultats pour {nom} ***")
    for matiere, groupe in zip(
        ["Français", "Anglais", "Mathématiques", "Physique"],
        [francais, anglais, math, physique],
    ):
        moyenne, echecs = calculer_moyenne_et_echecs(groupe)
        print(f"{matiere}: Moyenne = {moyenne:.2f}, Échecs = {echecs}")

# Résultats pour les filles
afficher_resultats("Filles", filles_francais, filles_anglais, filles_math, filles_physique)

# Résultats pour les garçons
afficher_resultats("Garçons", garcons_francais, garcons_anglais, garcons_math, garcons_physique)


