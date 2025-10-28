#nested for loops

#example 1
for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


#example 2
teams=['Dragon', 'Njauro', 'IMU', 'Xebec']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print("Matchup: " + home_team + " vs " + away_team)


#example 3
greeting="Hello"
for i in range(len(greeting)):
    print(i)


#example 4
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)


#example 5
for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")


#example 6
for x in range(7):
    if x % 2 == 0:
        print(x)
# The loop should print 0, 2, 4, 6

# As a list comprehension:
even_numbers = [x for x in range(7) if x % 2 == 0]
print(even_numbers)