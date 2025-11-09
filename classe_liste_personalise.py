class ListePerso:

    def __init__(self, nombres):
        self.nombres = []
        for nombre in nombres:
            if type(nombre) == int or type(nombre) == float:
                self.nombres.append(nombre)
            else:
                print(f"Opération interdite : il n'est pas possible d'initialiser la liste avec {nombre}")

    def append(self, nombre):
        if type(nombre) == int or type(nombre) == float:
            if nombre not in self.nombres:
                self.nombres.append(nombre)
            else:
                return f"Le nombre {nombre} existe déjà dans la liste"
        else:
            return f"Opération interdite : il n'est pas possible de rajouter le type {type(nombre)} dans la liste"

    def __str__(self):
        return f"{self.nombres}"

# Demander la taille de la liste
taille = int(input("Combien de nombres voulez-vous entrer ? "))

# Création de la liste à partir de la saisie utilisateur
valeurs = []
for i in range(taille):
    val = input(f"Saisir le nombre {i+1} : ")
    # Vérifie que c'est bien un nombre (sans try)
    if val.replace('.', '', 1).isdigit() or (val.startswith('-') and val[1:].replace('.', '', 1).isdigit()):
        # Conversion en int ou float
        if '.' in val:
            val = float(val)
        else:
            val = int(val)
        valeurs.append(val)
    else:
        print(f"'{val}' n'est pas un nombre valide, il est ignoré.")

# Création de l'objet ListePerso
L1 = ListePerso(valeurs)

# Affichage initial
print("Contenu initial :", L1)

# Ajout de 3 nouveaux éléments
for j in range(3):
    val = input(f"Saisir un nombre à ajouter ({j+1}/3) : ")
    if val.replace('.', '', 1).isdigit() or (val.startswith('-') and val[1:].replace('.', '', 1).isdigit()):
        if '.' in val:
            val = float(val)
        else:
            val = int(val)
        message = L1.append(val)
        if message:
            print(message)
    else:
        print(f"'{val}' n'est pas un nombre valide, ajout refusé.")

# Affichage final
print("Contenu final :", L1)
