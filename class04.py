# #String 

str1="This is a string"
str2='This is also a string'
str3="""This is also a string"""

print(len(str1))
print(str3[6])

#Slicing
str="Morsalin"
print(str[1:5]) #start=1(o) and end=5(l)
str4="Google"
print(str4[1:4])

print(str[-5:-2]) #Negative index 
print(str4[-5:-3])

#Conditional Statements
age= int(input("Enter your age: "))
if (age>=18):
    print("You are an adult.")
else:
    print("You are not an adult.")