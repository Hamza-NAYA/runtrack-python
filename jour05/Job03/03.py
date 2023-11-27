
def draw_triangle(height):
    for i in range(0, height + 1):
        if i != height:
            print(" "*(height - i) + "/" + " " * (i * 2) + "\\")
        if i == height:
            print("/" + "_" * height * 2 + "\\")


height = int(input("Entrez la hauteur de votre triangle : "))
real_height = height - 1

draw_triangle(real_height)