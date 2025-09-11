
#Membership Operators

num1 = int(input("Enter a number : "))
list = [10,20,30,40,50,60]
print(num1 in list)
print(num1 not in list)

x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
if(x is y):
    print("Same object")
elif(x is not y):
    print("Not same object")