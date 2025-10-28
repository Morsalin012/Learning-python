#multiple string variables on a single line to form a sentence
salutation = "Dr."
first_name = "Muhammad"
last_name = "Morsalin"
suffix = "Ph.D."
print(salutation + " " + first_name + " " + last_name + ", " + suffix)
print(salutation, first_name, last_name, ",", suffix)


#number to string
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is " + str(average)) #here average is converted to string

#string to number
str_num1 = "1024"
str_num2 = "3.1416"

result = str_num1 + str_num2
print("The result is " + str(result)) #here result is converted to string


# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests

print("Each person needs to pay: " + str(share_per_person)) # change a data type