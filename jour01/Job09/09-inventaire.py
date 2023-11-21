
class Produit:
    def __init__(self, nom, prix_unitaire, quantité_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantité_stock = quantité_stock

    def produit_informations(self):

        print(f"\nProduit: {self.nom}")
        print(f"Prix unitaire: {self.prix_unitaire} €")
        print(f"Quantité en stock: {self.quantité_stock} unités\n")

    def produit_inflation_informations(self):

        print(f"\nProduit: {self.nom}")
        print(f"Nouveau prix unitaire: {self.prix_unitaire} €")
        print(f"Quantité restante: {self.quantité_stock} unités\n")

    def produit_prix_mis_à_jour(self):
        self.prix_unitaire += self.prix_unitaire * 0.1

    def produit_stock_mis_à_jour(self, quantité_achetée):
        if self.quantité_stock >= quantité_achetée:
            self.quantité_stock -= quantité_achetée
        else:
            print("\nDésolé, la quantité demandée n'est pas disponible.")


inventaire = [ Produit("Chaise", 20, 5), Produit("Canapé", 800, 3), Produit("Table", 200, 15), Produit("Armoire", 350, 25), Produit("Table basse", 150, 65)]

print("\nBienvenue dans notre boutique de moblier, voici nos produits:\n")
for i, produit in enumerate(inventaire, 1):
    print(f"{i}-{produit.nom}")

choix_produit = (int(input("\nQuels produits voulez-vous ? Tapez son numéro pour le choisir: ")) - 1)

produit_choisi = inventaire[choix_produit]

produit_choisi.produit_informations()

quantité_achetée = int(input("Entrez la quantité de produits à acheter : "))

produit_choisi.produit_stock_mis_à_jour(quantité_achetée)

produit_choisi.produit_prix_mis_à_jour()

print("\nAprès l'inflation: ")

produit_choisi.produit_inflation_informations()