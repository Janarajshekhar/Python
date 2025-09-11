
#Check a number is prime or not

import math
num = int(input("Enter a number : "))
if num<0:
    print("Nagative number is not prime number")
elif num==1:
    print("1 is not prime and not composit")
else:    
    prime = True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            prime = False
            break
    if prime:
        print(num," is a prime number")
    else:
        print(num," is not a prime number") 