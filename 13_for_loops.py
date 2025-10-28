#for loop

#example 1
values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))


#example 2
product = 1
for n in range(1,10):
  product = product * n
  print(product)

print("Total product=",str(product))


#example 3
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))


#example 4
for x in range(2, -2, -1):
    print(x)