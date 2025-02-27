def somSousList(L,i,j):

 somme = 0
 b = L[i : j+1]
 for a in  b:

        somme = somme + a

 print(somme)


L = [10,20,30,40,50,60,70]

somSousList(L,0,2)