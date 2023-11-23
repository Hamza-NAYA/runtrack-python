
def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro impossible"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Modulo par zéro impossible"
    else:
        return "L'opérateur choisi n'est pas valide"


test = calcule(2, "/", 0)
print(test)
