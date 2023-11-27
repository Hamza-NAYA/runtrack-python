
def draw_rectangle(width, height):
    width_element = "-"
    height_element = "|"
    empty = " "

    for i in range(0, height) :
        if (i == 0 or i == (height - 1)):
            print(height_element + width_element * width + height_element)
        else:
            print(height_element + empty * width + height_element)

width = int(input("Entrez la largeur de votre rectangle : "))
height = int(input("Entrez la longueur de votre rectangle : "))

draw_rectangle(width, height)