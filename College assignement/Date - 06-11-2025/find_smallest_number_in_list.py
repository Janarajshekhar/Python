# Take list input from user
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Assume the first number is the smallest
smallest = numbers[0]

# Loop through the list to find the smallest number
for num in numbers:
    if num < smallest:
        smallest = num

print("The smallest number in the list is:", smallest)
