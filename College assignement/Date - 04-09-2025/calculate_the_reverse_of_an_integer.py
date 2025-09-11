
#calculate_the_reverse_of_an_integer

a=int(input("Enter a integer: "))
reverse_num=0
while a>0:
    digit=a%10
    reverse_num=reverse_num*10+digit
    a//=10
print("Reversed integer: ",reverse_num)