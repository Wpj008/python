def unionList(L1,L2,L3):

    L = L1 + L2 +L3
# la structure list(set(nom de la liste)) permet de supprimer les doublons
    L4 = list(set(L))
#la fonction sorted permet que la liste soit trier en ordre
    LF = sorted(L4)

    print(f'Liste après tri :{LF}')


La = [1,2,4,5,3,1]
Le = [1,2,3,2,1,2,1,8]
Lo = [6,7,9,0,6,4]


unionList(La,Le,Lo)