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
 