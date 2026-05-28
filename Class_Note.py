class Note:

    def __init__(self, nomEtudiant, notEtudiant):

        self.nomEtudiant = nomEtudiant
        self.notEtudiant = notEtudiant

    def a_reussi(self):

        if self.notEtudiant >= 75:

            print(f"L'etudiant {self.nomEtudiant} a reussi avec {self.notEtudiant} points")

        else:

            print(f"L'etudiant {self.nomEtudiant} a échoué avec {self.notEtudiant} points")

saisie1 = input("Saisir le nom de l'étudiant : ")
saisie2 = int(input(f"Saisir la note de l'etudiant {saisie1} : "))

saisie3 = input("Saisir le nom de l'étudiant : ")
saisie4 = int(input(f"Saisir la note de l'etudiant {saisie3} : "))

saisie5 = input("Saisir le nom de l'étudiant : ")
saisie6 = int(input(f"Saisir la note de l'etudiant {saisie5} : "))

etudiant1 = Note(saisie1, saisie2 )

etudiant2 = Note(saisie3, saisie4 )

etudiant3 = Note(saisie5, saisie6 )

etudiant1.a_reussi()
etudiant2.a_reussi()
etudiant3.a_reussi()