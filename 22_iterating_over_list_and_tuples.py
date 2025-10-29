# Iterating over a list and tuples

#example 1
animals=["Lion", "Zebra", "Dolphin", "Monkey"]
chars=0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))


#example 2
winners=["Ashley", "Dylan", "Essa"]
for index, person in enumerate(winners): #enumerate returns both index and value
    print("{} - {}".format(index+1, person))


#example 3
def full_emails(people):
    result=[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
print(full_emails([("ashley@egmail.com", "Ashley"),("dylan@egmail.com", "Dylan"),("essa@egmail.com", "Essa")]))