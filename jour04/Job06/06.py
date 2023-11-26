
numbers_list = []

for i in range(1, 6):
    numbers_list.append(i)

print(numbers_list)

first_value = numbers_list[0]
last_value = numbers_list[-1]

numbers_list[0] = last_value
numbers_list[-1] = first_value

print(numbers_list)