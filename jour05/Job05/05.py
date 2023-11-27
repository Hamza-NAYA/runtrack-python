
def decaler_message(message, decalage):
    message_encodé = ""

    for lettre in message:
        if lettre.isalpha():
            lettre_encodé = chr((ord(lettre.lower()) - ord('a') + decalage) % 26 + ord('a'))
            if lettre.isupper():
                lettre_encodé = lettre_encodé.upper()
            message_encodé += lettre_encodé
        else:
            message_encodé += lettre
    return message_encodé

test = decaler_message("Aller l'OM !", 3)
print(test)