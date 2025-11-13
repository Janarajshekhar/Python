# Program: Sum of Cubes of First N Natural Numbers Using Function
# Description: This program calculates the sum of cubes of natural numbers up to 'n' using a function.
# Author: [Your Name]
# Date: [Date]

def sum_of_cubes(n):
    # """Function to return sum of cubes of first n natural numbers"""
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total

# --- main part of program ---
a = int(input("Enter a number: "))
result = sum_of_cubes(a)
print("Sum of cubes:", result)
