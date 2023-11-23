
def verif(nombre):
    if nombre == int(nombre) and nombre > 0:
        if nombre % 2 == 0:
            print("Le nombre est paire")
        else:
            print("Le nombre est impaire")
    else:
        print("Le nombre n'est pas un entier positif")

verif(2)
verif(3)
verif(3.2)
