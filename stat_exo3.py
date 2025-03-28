#utilisation calcul de la moyenne
import numpy as np
import pandas as pd

donnee = np.array([1,2,3,4,5])

moyenne = np.mean(donnee)

print(f"La moyenne est de {moyenne}")


donnes = pd.read_csv("Etudiant.csv")

donnes["Moyenne"] = (donnes["Note1"]+donnes["Note2"]) / 2

donnes.to_csv("notes_avec_moyennes.csv", index=False)

print(donnes)