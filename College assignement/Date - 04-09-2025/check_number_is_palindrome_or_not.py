
#check palindrome number

num1 = int(input("Enter a number : "))
num2 = num1
reversed = 0
num = abs(num1)
while num1 != 0:
    reversed = ((reversed*10)+(num1%10))
    num1//=10
if num1 < 0:
    reversed = -reversed
if num2 == reversed :
    print(num2," is palindrome number")
else:
    print(num2," is not palindrome number") 