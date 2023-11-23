
def reverse(string):
    # deux methodes possibles
    new_string_methode1 = "".join(reversed(string))
    new_string_methode2 = string[::-1]
    print(new_string_methode2)

string = input("Entrez la chaine de caractère à inverser: ")

reverse(string)