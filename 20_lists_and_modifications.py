# List
# Modifying the contents of a list

#Example 1
fruits = ["Pineapple", "Banana", "Apple", "Melon", "Jackfruit", "Mango", "Kiwi"]
fruits.append("Grapes")
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Apple")
fruits.pop(5)
fruits[2] = "Strawberry"
print(fruits)