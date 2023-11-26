
def my_long_word(nombre, string):
    words = []
    word = ""

    for i in string:
        if i.isalpha():
            word += i
        elif word:
            length= 0
            for _ in word:
                length+= 1
            if length > nombre:
                words.append(word)
            word = ""
    phrase = " ".join(words)
    return phrase

test = my_long_word(5, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(test)