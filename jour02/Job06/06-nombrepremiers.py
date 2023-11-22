
for nombre in range(1, 1001, 1):
   if nombre > 1:
        for i in range(2, nombre):
            if (nombre % i) == 0:
               break
        else:
            valeur = nombre
            print(str(valeur) + " est un nombre premier")




