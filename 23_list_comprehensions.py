##List Comprehensions

#Example 1
languages =["python", "c++", "ruby", "java", "R", "C"]
lengths=[len(language) for language in languages]
print(lengths)

#Example 2
multiples=[]
for x in range(0,11):
    multiples.append(x*3)
print(multiples)


#Example 3
z=[x for x in range(0,101) if x%4==0]
print(z)


#Example 4
def odd_numbers(n):
	return [x for x in range(1, n+1) if x%2 !=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
