
def recolte(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et wiki")
    if type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    if type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    if type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")

recolte("fruits", "hiver")
recolte("fruits", "ete")
recolte("legume", "hiver")
recolte("legume", "ete")