
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

new_L = []

while L:
    value_min = L[0]
    for i in L:
        if i < value_min:
            value_min = i
    L.remove(value_min)

    value_min_int = int(value_min)
    value_min_float = value_min - value_min_int

    if value_min_float >= 0.5:
        value_min_float = 1
    else:
        value_min_float = 0
    new_value = value_min_int + value_min_float
    new_L.append(new_value)

print(new_L)