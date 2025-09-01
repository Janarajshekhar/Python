
#Find factorial

num1 = int(input("Enter first number : "))
fact = 1
if num1 < 0:
    print("Factorial does not exist for nagative number")
elif num1 == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num1+1):
        fact = fact*i
    print(f"The factorial of {num1} is {fact}") 