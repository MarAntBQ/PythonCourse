import math
number = int(input("Please insert an integer number: "))

while number <= 0:
    print(f"{number} is not positive")
    number = int(input("Please insert an positive number: "))

# The result should be integer not float
print(f"The square root of {number} is {int(math.isqrt(number))}")