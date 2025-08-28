
# Calculate area of triangle

import math
a = float(input("Enter the length of the first side : "))
b = float(input("Enter the length of the second side : "))
c = float(input("Enter the length of the third side : "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle is : ",area)