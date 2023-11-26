
L = [7, 11, 42, 39, 2, 5]

new_L = []

while L:
    value_min = L[0]
    for i in L:
        if i < value_min:
            value_min = i
    L.remove(value_min)
    new_L.append(value_min)

print(new_L)