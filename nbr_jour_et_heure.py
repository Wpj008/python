from datetime import datetime

def JourHeure(dateDebut, dateFin):
    format_date = "%d/%m/%Y"
    date_debut_format = datetime.strptime(dateDebut, format_date)
    date_fin_format = datetime.strptime(dateFin, format_date)
    nombre_jour = (date_fin_format - date_debut_format).days
    nombre_heure = nombre_jour * 24
    return nombre_jour, nombre_heure


dateDebut = input("Saisir la date de début (jj/mm/aaaa) : ")
dateFin = input("Saisir la date de fin (jj/mm/aaaa) : ")

# Appeler la fonction et afficher le résultat
jours, heures = JourHeure(dateDebut, dateFin)
print(f"Nombre de jours : {jours}")
print(f"Nombre d'heures : {heures}")
