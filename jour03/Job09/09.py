
def moyenne(note1, note2, note3):
    moyenne = (float(note1) + float(note2) + float(note3)) / 3
    return moyenne

note1 = float(input("Entrez la premiere note: "))
note2 = float(input("Entrez la seconde note: "))
note3 = float(input("Entrez la troisieme note: "))

moyenne_etudiant = moyenne(note1, note2, note3)

if moyenne_etudiant >= float(15) and moyenne_etudiant <= float(20):
    print("Très bon élève")
elif moyenne_etudiant >= float(11) and moyenne_etudiant <= float(14):
    print("Bon élève")
elif moyenne_etudiant >= float(8) and moyenne_etudiant <= float(10):
    print("Elève moyen")
else:
    print("Elève devant faire des efforts")