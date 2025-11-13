# Fibonacci Series without function

n=int(input("Enter a number: "))


a, b = 0, 1
odd = []
even = []

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")

    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

    a, b = b, a + b

print("\n\nOdd Fibonacci numbers:", odd)
print("Even Fibonacci numbers:", even)



#n=int(input("Enter a number: "))
#
#a,b=0,1
#
#while b<n :
#    a,b=b,a+b
#if b==n or n==0 :
#    print(n,"is a fibonacci number")
#else :
#    print(n,"is not a fibonacci number")

#Example: 0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13