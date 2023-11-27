
def phare(marches, hauteur):
    # On calcule la distance parcourue d'un aller
    distance_parcouru = marches * hauteur
    # On multiplie par le nombre de trajets or il parcoure à chaque fois deux fois la même distance
    distance_parcouru_jour = distance_parcouru * 5 * 2
    # Ensuite, on souhaite avoir la distance dans la semaine
    distance_parcouru_semaine_en_cm = distance_parcouru_jour * 7
    # Enfin, on convertit notre distance parcourue dans la semaine en mètres
    distance_parcouru_semaine_en_m = distance_parcouru_semaine_en_cm * (10**-2)

    # On return au format demandé dans le job
    resultat = "Pour " + str(marches) + " marches de " + str(hauteur) + " cm, le gardien parcourt " + str(distance_parcouru_semaine_en_m) + " m par semaine"
    return resultat

test = phare(307, 16)
print(test)