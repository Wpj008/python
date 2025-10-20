def separer(L):

    nbr_0 = L.count(0)

    nbr_1 = L.count(1)

    L1 = [0] * nbr_0 + [1] * nbr_1

    return L1

print(separer([1,0,0,0,1,1,1,0,1,1,0,0,0,1]))