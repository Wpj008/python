# print("Hello, world") 

# gauche = 8 
# droite = 4 
# signe = "/"

# if signe == "+" :

#          somme = gauche - droite
         
#          print(somme)
         
# elif signe == "-" :

#     dif = gauche - droite
    
#     print(dif)
    
# elif signe == "*" : 
        
#         pro = gauche * droite
        
#         print (pro)
        
# elif signe == "/" : 
            
#             div = gauche / droite 
            
#             print (div)
         


#          #Créez une fonction appelée  salaire_mensuel(salaire_annuel)  qui prend en paramètre un salaire annuel et retourne le salaire mensuel correspondant en divisant le salaire annuel par 12.
# def salaire_mensuel(salaire_annuel) :
    
#     salaire_mensuel = salaire_annuel / 12
    
#     return salaire_mensuel
# #Créez une fonction appelée  salaire_hebdomadaire(salaire_mensuel)  qui prend en paramètre un salaire mensuel et retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4.
# def salaire_hebdomadaire(salaire_mensuel) : 
    
#     salaire_hebdomadaire = salaire_mensuel / 4 
    
#     return salaire_hebdomadaire

# #Créez une fonction appelée  salaire_horaire(salaire_hebdomadaire, heures_travaillees)  qui prend en paramètres un salaire hebdomadaire et le nombre d'heures travaillées par semaine, et retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par le nombre d'heures travaillées par semaine.
# def salaire_horaire(salaire_heb, heure_travail) :

#     salaire_horaire = salaire_heb / heure_travail

#     return salaire_horaire 
# #Demandez à l'utilisateur de saisir son salaire annuel.
# salaire_annuel = 12000
# #Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine.
# heures_travail = 40

# #Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant.

# salaire_mensuel(12000)

# salaire_hebdomadaire(salaire_mensuel)

# salaire_horaire(salaire_hebdomadaire, heures_travail)
# #Affichez le résultat sous la forme : "Votre salaire horaire est de XX euros".

# print(f"Votre salaire horaire est de {salaire_horaire}")

# # Définir le moyenne autorisée
# moyenne_autorisee = 10
# # Exemple de résultats pour chaque discipline (filles et garçons)
# resultats = {
#     'Maths': {'filles': [12, 15, 9, 14, 10],  'garçons': [8, 16, 10, 11, 13]},
#     'Physique': {'filles': [10, 12, 8, 14, 9], 'garçons': [11, 15, 10, 8, 12]},
#     'Français': {'filles': [16, 17, 15, 14, 18], 'garçons': [14, 16, 13, 12, 15]},
#     'Anglais': {'filles': [14, 13, 12, 15, 16], 'garçons': [15, 14, 13, 12, 10]}
# }
# # Fonction pour calculer la moyenne
# def calculer_moyenne(notes):
#     return sum(notes) / len(notes)
# # Fonction pour calculer le nombre d'échecs
# def calculer_echecs(notes, moyenne):
#     total = len([note for note in notes if note < moyenne_autorisee])
    
#     return total
# # Fonction pour afficher les résultats
# def afficher_resultats():
#     disciplines = ['Maths', 'Physique', 'Français', 'Anglais']
    
#     for discipline in disciplines:
#         print(f"\nDiscipline: {discipline}")
        
#         for genre in ['filles', 'garçons']:
#             # Moyenne pour chaque genre dans chaque discipline
#             moyenne = calculer_moyenne(resultats[discipline][genre])
#             print(f"  Moyenne des {genre} : {moyenne:.2f}")
            
#             # Nombre d'échecs pour chaque genre dans chaque discipline
#             echecs = calculer_echecs(resultats[discipline][genre], moyenne_autorisee)
#             print(f"  Nombre d'échecs des {genre} : {echecs}")
# # Exécuter le programme
# afficher_resultats()

# # Exemple de données (vous pouvez les remplacer par un fichier réel)
# mouvements = [
#     {"DATEMVT": "2024-12-01", "CODESUCURSSALE": "001", "NOMCLIENT": "Jean Dupont", "CODEMVT": "D", "MONTANT": 500},
#     {"DATEMVT": "2024-12-01", "CODESUCURSSALE": "001", "NOMCLIENT": "Marie Dubois", "CODEMVT": "R", "MONTANT": 200},
#     {"DATEMVT": "2024-12-02", "CODESUCURSSALE": "002", "NOMCLIENT": "Paul Martin", "CODEMVT": "D", "MONTANT": 700},
#     {"DATEMVT": "2024-12-02", "CODESUCURSSALE": "002", "NOMCLIENT": "Lisa Durand", "CODEMVT": "R", "MONTANT": 300}
# ]

# # Trier les mouvements par date
# mouvements = sorted(mouvements, key=lambda x: x["DATEMVT"])

# # Initialisation des totaux généraux
# total_depots_generaux = 0
# total_retraits_generaux = 0

# # Grouper les mouvements par date
# dates_traites = set()  # Pour garder trace des dates déjà traitées

# for mouvement in mouvements:
#     date = mouvement["DATEMVT"]

#     if date not in dates_traites:
#         # Une nouvelle date commence
#         print(f"\nDate : {date}")
#         print("-" * 50)

#         # Filtrer les mouvements pour cette date
#         mouvements_date = [m for m in mouvements if m["DATEMVT"] == date]

#         # Initialisation des totaux pour cette date
#         total_depots = 0
#         total_retraits = 0

#         for mvt in mouvements_date:
#             # Afficher les informations de chaque mouvement
#             print(f"Succursale : {mvt['CODESUCURSSALE']}, Client : {mvt['NOMCLIENT']}, Montant : {mvt['MONTANT']}")

#             # Calculer les totaux pour cette date
#             if mvt["CODEMVT"] == "D":
#                 total_depots += mvt["MONTANT"]
#             elif mvt["CODEMVT"] == "R":
#                 total_retraits += mvt["MONTANT"]

#         # Calculer le solde pour cette date
#         solde = total_depots - total_retraits

#         # Imprimer les totaux pour cette date
#         print("\nRésumé pour cette date :")
#         print(f"Total dépôts : {total_depots}")
#         print(f"Total retraits : {total_retraits}")
#         print(f"Solde : {solde}")

#         # Ajouter aux totaux généraux
#         total_depots_generaux += total_depots
#         total_retraits_generaux += total_retraits

#         # Marquer la date comme traitée
#         dates_traites.add(date)

#         # Ajouter une séparation (comme un saut de page)
#         print("\n" + "=" * 50)

# # Calculer les totaux généraux
# solde_general = total_depots_generaux - total_retraits_generaux

# # Afficher les totaux généraux
# print("\nRésumé général :")
# print("-" * 50)
# print(f"Total général dépôts : {total_depots_generaux}")
# print(f"Total général retraits : {total_retraits_generaux}")
# print(f"Solde général : {solde_general}")



# # Introduction5

# print("Nous allons comparer les performances des garçons et des filles dans différentes matières.")

# # Initialisation des matières avec des tableaux séparés pour chaque groupe
# filles_francais = []
# filles_anglais = []
# filles_math = []
# filles_physique = []

# garcons_francais = []
# garcons_anglais = []
# garcons_math = []
# garcons_physique = []

# # Fonction pour entrer les notes
# def collecter_notes(nom_matiere, groupe):
#     print(f"\nEntrez les notes pour {nom_matiere}. Tapez '-1' pour arrêter.")
#     while True:
#         try:
#             note = float(input("Note : "))
#             if note <= -1:  # Arrêter la saisie
#                 break
#             groupe.append(note)
#         except ValueError:
#             print("Veuillez entrer une note valide.")

# # Collecte des données pour les filles
# print("\n*** Notes des Filles ***")
# collecter_notes("français", filles_francais)
# collecter_notes("anglais", filles_anglais)
# collecter_notes("mathématiques", filles_math)
# collecter_notes("physique", filles_physique)

# # Collecte des données pour les garçons
# print("\n*** Notes des Garçons ***")
# collecter_notes("français", garcons_francais)
# collecter_notes("anglais", garcons_anglais)
# collecter_notes("mathématiques", garcons_math)
# collecter_notes("physique", garcons_physique)

# # Fonction pour calculer la moyenne et les échecs
# def calculer_moyenne_et_echecs(groupe):
#     if len(groupe) == 0:  # Éviter la division par zéro
#         return 0, 0
#     moyenne = sum(groupe) / len(groupe)
#     echecs = sum(1 for note in groupe if note < 10)
#     return moyenne, echecs

# # Affichage des résultats
# def afficher_resultats(nom, francais, anglais, math, physique):
#     print(f"\n*** Résultats pour {nom} ***")
#     for matiere, groupe in zip(
#         ["Français", "Anglais", "Mathématiques", "Physique"],
#         [francais, anglais, math, physique],
#     ):
#         moyenne, echecs = calculer_moyenne_et_echecs(groupe)
#         print(f"{matiere}: Moyenne = {moyenne:.2f}, Échecs = {echecs}")

# # Résultats pour les filles
# afficher_resultats("Filles", filles_francais, filles_anglais, filles_math, filles_physique)

# # Résultats pour les garçons
# afficher_resultats("Garçons", garcons_francais, garcons_anglais, garcons_math, garcons_physique)

# # Conclusion
# print("\nComparez les moyennes et les échecs pour conclure sur le préjugé.")

