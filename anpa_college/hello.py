
# num1=int(input("Enter first number : "))
# num2=int(input("Enter second number : "))
# sum=num1+num2
# print("sum = ", sum)

# side=float(input("Enter side of a square : "))
# print("Area of square is : ",side*side)

# num1=float(input("Enter first number : "))
# num2=float(input("Enter second number : "))
# avg=(num1+num2)/2
# print("sum = ", avg)

# num1=int(input("Enter first number : "))
# num2=int(input("Enter second number : "))
# if(num1>=num2):
#     print(True)
# else:
#     print(False)

# name1=str("hello")
# name2=str("world")
# print(name1+name2)
# print(len(name1))
# print(name1[1:4])
# print(name1[-4:-2])

# str="i am studying"
# print(str.endswith("ing"))
# print(str.capitalize())
# print(str.replace("i", "a"))
# print(str.find("u"))
# print(str.find("am"))
# print(str.count("i"))

# age = 21
# if(age >= 18):
#     print("appli for license")
# elif()


# -----------List--------value change
# marks=[94.4, 84.6, 23.7, 67.9, "rajshekhar"]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])
# print(marks[4])
# print(marks[2:4]) #---------------------list slicing

# list = [2,4,8,5]
# list.append(7)
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

# list.reverse()
# print(list)

# list.insert(3, 9)
# print(list)

# list.remove(4)
# print(list)

# list.pop(3)
# print(list)


# ------Tuples---- value not change
# tup=(45,67,89,23,56,78)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# tup[0]=5 #Error

# tup1 = (3) #integer
# tup2 = (3,) #tuple
# print(type(tup1))
# print(type(tup2))

# tup=(2,1,3,1,3,3)
# print(tup.index(3))
# print(tup.count(3))




# --------------dictinary----------------

# info = {
#     "name" : "rajshekhar jana",
#     "subject" : ["C", "C++", "Java", "Python"], #list
#     "topics" : ("dict", "set")
# }
           ## #dic = {}    # impty dictinary
# # print(info)
# # print(type(info))
# # print(info["name"])
# # print(info["topics"])
# # print(info.keys())
# # print(info.values())
# # print(info.items())
# # print(info.get("name"))
# info.update({"city" : "kolkata"})
# print(info)



### ----------------------set----------------------
###set is unorder 

# collection = {1,2,3,4,5}
# print(collection)
# print(type(collection))

# collection = {1,2,3,4,5, "Hello", "World"}
# print(collection)
# print(type(collection))

# collection = {1,2,2,4,2, "Hello", "World", "World"}
# print(collection)             #ignore dublicate value
# print(type(collection))
# print(len(collection))

#collection = {}  # it is a empty dictinary not empty set
# collection = set()   #empty set


# collection = set()

# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(2)   # ignore dublicate value 

# print(collection)

# collection.remove(1)
# print(collection)

# collection.clear()
# print(len(collection))


# collection = {"hello", "apple", "coding", "python", "world"}
# print(collection.pop())

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))
# print(set1) #original value not change
# print(set2) #original value not change


# print(set1.intersection(set2))