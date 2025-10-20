#Defining Functions

def greetings(name):
    print("Welcome, " + name)
    
greetings("Kay")
greetings("Cameron")

def greeting(name, department):
    print("Welcome, "+ name)
    print("You are part of "+ department)

greeting("Blake", "Software Engineering")
greeting("Ellis", "Data Science")



#Function with return value
def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))


#Function with multiple return values
def lucky_number(name):
    number = len(name)*9
    print("Hello " + name + ", your lucky number is "+ str(number))
lucky_number("Morsalin")


# #Exercise: Function to calculate total days
def find_total_days(years, months, days):
    find_total_days_days = (years*365) + (months*30) + days
    return find_total_days_days
print(find_total_days(2,5,23))