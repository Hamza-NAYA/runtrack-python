
def diagonale(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j == n:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()

nbr_ligne = int(input("Entrez le nombre de ligne et de colonne : "))

diagonale(nbr_ligne)