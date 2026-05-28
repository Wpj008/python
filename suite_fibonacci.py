'''def suiteFibonacci(N):

    if N<= 2:

        return 1
    
    return suiteFibonacci(N-1) + suiteFibonacci(N-2)

saisie = int(input("Saisir un nombre : "))

print(suiteFibonacci(saisie)) '''

# Programme pour générer la suite de Fibonacci en utilisant la récursivité

'''def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = int(input("Entrez le nombre de termes:"))

print("Suite de Fibonacci en utilisant la recursion :")
for i in range(n):
    print(fibonacci(i))'''

nterms = int(input("Entrez un nombre: "))
 
n1 = 0
n2 = 1
 
print("\n la suite fibonacci est :")
print(n1, ",", n2, end=", ")
 
for i in range(2, nterms):
  suivant = n1 + n2
  print(suivant, end=", ")
 
  n1 = n2
  n2 = suivant