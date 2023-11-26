
def list_fruit():
    fruits = ['pomme','cerise','orange','Melon']
    fruits.insert(2,'Mangue')
    return fruits

test = list_fruit()
print(test)