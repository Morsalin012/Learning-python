# Problem solving of class 4 and 5

# input users surname and print its length
firstName=input("Enter your first name: ")
SurName=input("Enter your surname: ")
print(len(SurName))

# #find the occurrence of "$" in a string
str="$$Morsalin$$"
print(str.count("$"))

# input mark from the user then print what the grade is
mark=float(input("Enter your mark: "))
if (mark>=90):
    print("Grade A")
elif (mark<90 and mark>=80):
    print("Grade B")
elif (mark<80 and mark>=70):
    print("Garde C")
else:
    print("Grade D")

#Odd/Even??
num=int(input("Enter any integer number for check: "))
if num%2==0:
    print("It is EVEN.")
else:
    print("Its ODD")

#Find the greatest of 3 numbers
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))

if a>b and a>c:
    print("Greatest number is: ", a)
elif b>a and b>c:
    print("Greatest number is: ", b)
else:
    print("Greatest number is: ", c)

#Check if a number is a multiple of 4
num=int(input("Enter any positive integer number: "))
if num%4==0:
    print("Its a multiple of 4")
else:
    print("No, its not a multiple of 4")