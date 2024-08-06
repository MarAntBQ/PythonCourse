number = 15
text = "Hello, World!"
# Print the type of the variables
print(type(number))
print(type(text))

# Output without <class>:
print(f"{number} is a var type as:", type(number).__name__)
print(f"{text} is a var type as:", type(text).__name__)
