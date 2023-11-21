
capital_initial = 10000
rendement = 5

#rendement brut = (gain_annuel / capital_initial) x 100
#pour avoir le gain on reprend la formule
#donc rendement brut / 100 = gain_annuel / capital_initial
#ainsi gain_annuel = rendement brut / 100 * capital_initial

gain_annuel = (rendement / 100) * capital_initial
print(f"\nGain annuel initial : {gain_annuel} €")

capital_initial += 5000
rendement += 2

nouveau_gain_annuel = (rendement / 100) * capital_initial
print(f"Nouveau gain annuel : {nouveau_gain_annuel} €")

retrait = capital_initial * 0.1
capital_initial -= retrait
rendement -= 1

#capital_initial_final = capital_initial_initial * (1 + rendement)puissance(nombre d'années)
#ici on considere 1 années donc puissance 1 ce qui revient à capital_initial_final = capital_initial_initial * (1 + rendement)
#capital_initial_final = capital_initial_initial * (1 + rendement)
#capital_initial_final = capital_initial_initial + capital_initial_inital * rendement
#or rendement = gain_annuel / capital_initial_inital
#capital_initial_final = capital_initial_initial + capital_initial_inital * (gain_annuel / capital_initial_inital)
#donc capital_initial_final = capital_initial_initial + gain_annuel

capital_initial_final = capital_initial + nouveau_gain_annuel
print(f"Montant final de l'investissement : {capital_initial_final} €")

nouveau_gain_final = (rendement / 100) * capital_initial_final
print(f"Nouveau gain après retrait : {nouveau_gain_final} €\n")