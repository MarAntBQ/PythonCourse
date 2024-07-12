# Get the radius of a circle
import math

pi = 3.14159265359

r = float(input("Insert the value of the radius: "))

l = 2*math.pi*r
print(f"The lenght is: {l:.1f}")

a = math.pi * r**2

print(f"The are of the circle is: {a:.1f}")