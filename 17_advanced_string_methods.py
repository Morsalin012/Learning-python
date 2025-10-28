#Some string methods
string1 = "Mountains"
print(string1.upper())#all letters to uppercase
print(string1.lower())#all letters to lowercase

print(" yes ".strip())#remove whitespace from both sides
print(" yes ".lstrip())#remove whitespace from left side
print(" yes ".rstrip())#remove whitespace from right side

print("The number of times e occurs in this string is 4".count("e"))#count occurrences of substring

print("Hello World".replace("World","There"))#replace substring with another substring

print("Forest".endswith("rest"))#check if string ends with a specific substring
print("Forest".startswith("For"))#check if string starts with a specific substring

print("Forest".isnumeric())#check if all characters in the string are numeric
print("12345".isnumeric())#check if all characters in the string are alphabetic

print("This is another example".split())#split string into a list of substrings based on whitespace

print("Forrest".isalpha())

weather= "rainfall"
print(weather[:4])