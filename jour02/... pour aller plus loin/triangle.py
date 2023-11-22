
L_a = int(input("Choisissez une longueur pour A :"))
L_b = int(input("Choisissez une longueur pour B :"))
L_c = int(input("Choisissez une longueur pour C :"))


if L_a <= 0 and L_b <= 0 and L_c <= 0:
    if (L_a**2 == L_b**2 + L_c**2) or (L_a**2 == L_b**2 + L_c**2) or (L_a**2 == L_b**2 + L_c**2):
        print("Le triangle est rectangle")
        if (L_a == L_b) or (L_a == L_c) or (L_b== L_c):
            print("Le triangle est rectangle isocèle")
    elif (L_a == L_b == L_c):
        print("Le triangle est équilateral")
    elif (L_a == L_b) or (L_a == L_c) or (L_b== L_c):
        print("Le triangle est isocèle")
    else:
        print("Le triangle est quelconque")
else:
    print("Les valeurs saisies sont infèrieurs ou égales à zéro")