def remplacement(phrase, Mot_1, Mot_2):

    if Mot_1 in phrase:

        debut_Mot_1 = phrase.index(Mot_1)

        fin_Mot_1 = debut_Mot_1 + len(Mot_1)

        phrase_list = list(phrase)

        phrase_list[debut_Mot_1:fin_Mot_1] = Mot_2

        phrase = "".join(phrase_list)

        print(phrase)

    return phrase

saisie = (input("Saisir une phrase : "))
saisie1 = (input("Saisir le mot à remplacer : "))
saisie2 = (input("Saisir le nouveau mot qui remplacera : "))

remplacement(saisie,saisie1,saisie2)