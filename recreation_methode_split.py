def fonction_split(phrase, caractere):
    phrase_list = []
    mot_tmp = ""

    if caractere in phrase:
        for i in range(len(phrase)):
            if phrase[i] != caractere:
                mot_tmp += phrase[i]
            else:
                phrase_list.append(mot_tmp)
                mot_tmp = ""
        # Ajouter le dernier mot après la boucle
        if mot_tmp:
            phrase_list.append(mot_tmp)
    else:
        phrase_list.append(phrase)

    return phrase_list

# Exemple d'utilisation
saisie = input("Saisir une phrase : ")
resultat = fonction_split(saisie, ",")
print(resultat)
