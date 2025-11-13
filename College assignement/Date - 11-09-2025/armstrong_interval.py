a=int(input("Enter lower limit number: "))
b=int(input("Enter higher limit number: "))


print(f"All Armstrong numbers are of this interval: ")
for i in range(a,b+1):
    n=len(str(i))
    temp=i
    sum=0

    while temp>0:
        digit=temp% 10
        sum+=digit**n
        temp//=10
    
    if i==sum:
        print(i)