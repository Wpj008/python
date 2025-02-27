def maximum(L):

    a = L[0]
    for i in L:

     if i > a:
          
          a = i
           
    print(f"la valeur maximale dans la liste est {a}")

L = [1,9,3,4,5]

maximum(L)