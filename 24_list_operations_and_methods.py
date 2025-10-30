# List operations and methods

# len(sequence) - Returns the number of elements in a sequence
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Outputs: 5

# for element in sequence - Loops through each element in a sequence
my_list = ['a', 'b', 'c']
for element in my_list:
    print(element)  # Outputs: a, b, c

# if element in sequence - Checks if an element exists in a sequence
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Outputs: True

# sequence[x] - Accesses the element at index x (starting from 0)
my_list = ['a', 'b', 'c', 'd']
print(my_list)  # Outputs: c

# sequence[x:y] - Extracts a slice from index x to y-1
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Outputs: [2, 3, 4]

# for index, element in enumerate(sequence) - Loops through both indices and elements
my_list = ['a', 'b', 'c']
for index, element in enumerate(my_list):
    print(index, element)  # Outputs: 0 a, 1 b, 2 c

# list[index] = x - Replaces an element at a specific index
my_list = [1, 2, 3]
my_list = 10
print(my_list)  # Outputs: [1, 10, 3]

# list.append(x) - Adds an element to the end of a list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Outputs: [1, 2, 3, 4]

# list.insert(index, x) - Inserts an element at a specific index
my_list = [1, 2, 4]
my_list.insert(2, 3)
print(my_list)  # Outputs: [1, 2, 3, 4]

# list.pop(index) - Removes and returns an element at a specific index
my_list = [1, 2, 3, 4]
removed = my_list.pop(2)
print(removed, my_list)  # Outputs: 3 [1, 2, 4]

# list.remove(x) - Removes the first occurrence of a value
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # Outputs: [1, 3, 2, 4]

# list.reverse() - Reverses the order of elements in a list
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)  # Outputs: [4, 3, 2, 1]

# list.clear() - Removes all elements from a list
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Outputs: []

# list.copy() - Creates a shallow copy of a list
my_list = [1, 2, 3]
my_copy = my_list.copy()
print(my_copy)  # Outputs: [1, 2, 3]

# list.extend(other_list) - Adds all elements from another list to the end
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Outputs: [1, 2, 3, 4, 5, 6]

# map(function, iterable) - Applies a function to each element in an iterable
def double(x):
    return x * 2
numbers = [1, 2, 3, 4]
result = list(map(double, numbers))
print(result)  # Outputs: [2, 4, 6, 8]

# zip(*iterables) - Combines multiple iterables into tuples
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)  # Outputs: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# tuple() - Converts an iterable into a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)  # Outputs: (1, 2, 3, 4)