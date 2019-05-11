with open('taroster.txt', 'r') as file:
    person = "^("

    for line in file:
        name = line
        person = person + name + "|"

    person = person + ")$"

with open('tavalidator.txt', 'w') as file:
    file.write(person)
