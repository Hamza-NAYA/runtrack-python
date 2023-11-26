
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

somme_liste = 0

for i in L:
    if i % 2 == 0:
        somme_liste += i

print(somme_liste)