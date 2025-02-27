def ajoutDictionnaire(d, cle, valeur):

    d[cle] = valeur

    print(d)


fruit = {
        "Pomme" : "vert",
        "Banane" :"Jaune",
        "Fraise" : "Rouge"
}      

ajoutDictionnaire(fruit, "Kiwi", "Marron")
ajoutDictionnaire(fruit, "orange", "orange")