# i=1
# while i<=5 :
#     print("hello")
#     i = i + 1
# print(i)


# i=1
# while i<=100 :
#     print(i)
#     i+=1


# i=100
# while i>=1 :
#     print(i)
#     i-=1


# num = int(input("Enter a number : "))
# i=1
# while i<=10:
#     print(num," * ",i," = ",num*i)
#     i=i+1


# nums = [1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(nums) :
#     print(nums[i])
#     i=i+1


# numss = (1,4,9,16,25,36,49,64,81,100) 
# # print(type(numss))
# print(numss)
# s=int(input("Enter search element : "))
# i=0
# while i<len(numss):
#     if numss[i]==s:
#         print("search element is found index no : ",i)
#     i=i+1


# i=1
# while i<=5 :
#     print(i)
#     if i==3:
#         break
#     i+=1
# print("end ")


# i=1
# while i<=5 :
#     if i==3:
#         i = i + 1
#         continue
#     print(i)
#     i += 1
# print("end ")


# list = [1,2,3,4,5]
# for val in list:
#     print(val)


# seq = range(5)
# for i in seq:
#     print(i)


# for i in range(10):
#     print(i)


# for i in range(10):  #range(stop)
#     print(i)


# for i in range(2,10):  #range(start,stop)
#     print(i)

# for i in range(2,10,2):  #range(start,stop,step)
#     print(i)


# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)


# num = int(input("Enter a number : "))
# for i in range(1,11):
#     print(i," * ",num," = ",num*i)


# for i in range(5):
#     #empty        ---------error---------
# print("something")

# for i in range(5):
#     pass
# print("something")


# num1 = int(input("Enter a number : "))
# sum=0
# i=1
# while i<=num1:
#     sum = sum + i
#     i=i+1
# print("sum = ",sum)


num1 = int(input("Enter a number : "))
fact=1
for i in range(1,num1+1):
    fact = fact * i
    i = i + 1
print("fact = ",fact)