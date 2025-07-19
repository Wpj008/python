def calculSomme(L):
    
    if len(L) == 0:
        return 0
    
    return L[0] +calculSomme(L[1:])

LI = [1,5,8,7,9,6]

print(f'la somme de tous les éléments de la liste vaut : {calculSomme(LI)}')