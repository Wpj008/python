#nombre maximal dans une list

def maximale(L):
    a = L[0]
    for i in L:
     if i > a:
        a = i

    return a 
     
L = [1,9,7,8,2,6] 

valeur = maximale(L)

print(f" la valeur maximale dans la liste est {valeur}")