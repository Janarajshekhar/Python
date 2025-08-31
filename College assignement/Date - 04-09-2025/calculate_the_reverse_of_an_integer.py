
#calculate_the_reverse_of_an_integer

num = int(input("Enter a number : "))
reversed = 0
num = abs(num)
while num != 0:
    reversed = ((reversed*10)+(num%10))
    num//=10
if num < 0:
    reversed = -reversed
print("reversed = ",reversed)
