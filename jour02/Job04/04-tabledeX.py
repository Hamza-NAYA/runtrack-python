
def table(num):
    print("Table de multiplication de " + str(num) + " :" )
    for number in range(1, 11, 1):
        produit = num * number
        table = str(num) + " x " + str(number) + " = " + str(produit)
        print(table)

entier_n = int(input("Entrez un entier supérieur à zéro (N) : "))

table(entier_n)
