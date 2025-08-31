
# Swap two number without using third variable

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("Before swap......")
print("num1 = ",num1," , num2 = ",num2)
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print("After swap......")
print("num1 = ",num1," , num2 = ",num2)