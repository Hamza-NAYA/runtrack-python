
def function(string):
    if "e" in string:
        return True
    else:
        return False

string_test = input("\nEntrez une chaîne de caractères: ")
reponse = function(string_test)

if reponse == True:
    print("\nLa chaîne contient le caractère << e >>\n")
else:
    print("\nLa chaîne ne contient pas le caractère << e >>\n")
