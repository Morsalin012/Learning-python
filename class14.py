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