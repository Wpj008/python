def pgcd():
    A = int(input("Saisir la première valeur : "))
    B = int(input("Saisir la deuxième valeur : "))

    if B == 0:
        print("La deuxième valeur doit être différente de 0 !")
        return  0

    A1 = A
    B1 = B
    
    while B != 0:
        R = A % B
        A = B
        B = R

    print(f"{A} est le PGCD des {A1} et {B1}.")

pgcd()
