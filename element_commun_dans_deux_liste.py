L1 = [9,8,7,14,3,2,"a","p","bonjour","b"]
L2 = ["b",1,9.2,6,3,9,"p"]
L3 = []

L3 = [x for x in L1 if x in L2]
#or ou  L3 = list(set(L1) & set(L2))
print(L3)
