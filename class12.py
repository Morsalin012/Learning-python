#Loops 

#While loop
#example 1
x=0
while x<5:
    print("Not there yet, x=" + str(x))
    x= x+1
print("x=" + str(x))

#example 2
def attempts(n):
    x=1
    while x<=n:
        print("Attempt " + str(x))
        x=x+1
    print("Done")
attempts(5)

#example 3
x=1
sum=0
while x<10:
    sum=sum+x
    x=x+1
print("Total sum =", sum)

product=1
while x<10:
    product=product*x
    x=x+1
print("Total product = ", product)
 

# example 4
def count_factors(given_number):
    factor=1
    count=1
    if given_number==0:
        return 0
    while factor<given_number:
        if given_number%factor==0:
            count+=1
        factor+=1
    return count
print(count_factors(0))
print(count_factors(2))
print(count_factors(4))
print(count_factors(6))
print(count_factors(10))

#Example 5
def addition_table(given_number):
    interated_number=1
    my_sum=1
    while interated_number<=5:
        my_sum= given_number+interated_number
        if my_sum>20:
            break
        print(str(given_number), "+", str(interated_number), "=", str(my_sum))
        interated_number+=1

addition_table(4)
addition_table(5)