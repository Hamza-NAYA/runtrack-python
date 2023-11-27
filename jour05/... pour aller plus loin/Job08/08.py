
def my_sort(liste):
    # On pose la variable n égale à la longueur de la liste cela va nous permettre l'adressage des index de la liste
    n = len(liste)
    # On initialise le compteur de coups
    coups = 0

    # On définit une variable d'état action qui va nous permettre d'exécuter notre programme tant que celui-ci n'est pas fini
    action = True

    # On utilise une boucle while pour trier notre liste et compter le nombre de coups
    while action:
        # la boucle white s'exécute tant que action = True or on veut que la boucle while prenne fin lorsque notre programme a fini de trier la liste
        # ainsi on assigne à la variable action l'état False pour vérifier que le tri est bien fini et ainsi mettre fin à notre boucle
        action = False
        # On met une range(n - 1) puisque l'on veut que i varie de l'index 0 au dernier index de la liste
        for i in range(n - 1):
            # on compare les éléments adjacents et on les déplace si nécessaire
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                # si un délacement a été effectué alors on fait la transition de la variable action de l'état False à l'état True
                action = True
                # Puisque la transition d'état a été effectuée alors on augmente de 1 le compteur de coups
                coups += 1
    # On return au format demandé dans le job
    liste_triée = ("Nombre total de coups nécessaires pour trier la liste : " + str(coups) + "\nListe triée : " + str(liste))
    return liste_triée

test = my_sort([90, 12, 25, 34, 11, 64, 22])
print(test)