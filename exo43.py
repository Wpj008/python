def minimum(L):
    
 minimum = L[0]

 for i in L:

        if i < minimum:
            minimum = i

 print(minimum)

L = [3,4,5,2,7]

minimum(L)