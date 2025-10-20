'''
Écris une fonction nettoyerPhrase(phrase) qui enlève :

tous les espaces,

tous les points,

et toutes les virgules.

Elle doit retourner la phrase “nettoyée”.
'''

def nettoyerPhrase(phrase):

    if " " in phrase:
        phrase = phrase.replace(" ","")

    if  "," in phrase :
     phrase = phrase.replace(",",":")

    if  "." in phrase:
     phrase = phrase.replace(".","!")

   

    print(phrase)

phrase = input("Saisir une phrase : ")

nettoyerPhrase(phrase)