def suiteFibonacci(N):

    if N<= 2:

        return 1
    
    return suiteFibonacci(N-1) + suiteFibonacci(N-2)

saisie = int(input("Saisir un nombre : "))

print(suiteFibonacci(saisie))