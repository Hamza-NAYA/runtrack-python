
numbers_list = []

for i in range(1, 6):
    numbers_list.append(i)

print(numbers_list)
print(numbers_list[1])

def function(liste):
    liste[3] = liste[2] + liste[4]
    print(liste)
    print(liste[-1])

function(numbers_list)