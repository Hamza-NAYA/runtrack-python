
L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

produit_liste = 1

for i in L:
    if i in range(25, 92):
        produit_liste *= i

print(produit_liste)