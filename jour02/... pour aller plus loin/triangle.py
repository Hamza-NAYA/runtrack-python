
a = float(input("Choisissez une longueur pour A : "))
b = float(input("Choisissez une longueur pour B : "))
c = float(input("Choisissez une longueur pour C : "))

#Pour savoir si l'on peut construire un triangle dont les longueurs des côtés sont données,
#il suffit de vérifier que la plus grande longueur est inférieure à la somme des deux autres.

if a + b > c and b + c > a and c + a > b:
    if (a**2 == b**2 + c**2) or (c**2 == b**2 + a**2) or (b**2 == a**2 + c**2):
        print("Le triangle est rectangle")
        if (a == b) or (a == c) or (b == c):
            print("Le triangle est rectangle isocèle")
    elif (a == b == c):
        print("Le triangle est équilateral")
    elif (a == b) or (a == c) or (b== c):
        print("Le triangle est isocèle")
    else:
        print("Le triangle est quelconque")
else:
    print("Les valeurs saisies ne permettent pas de former un triangle")