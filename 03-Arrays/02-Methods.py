students = ["Marco Antonio", "Ana Verónica", "David Alexander", "Marco Vinicio"]


# How to get the length using len(array) //
print(len(students))

# Add one student to the end
students.append("Mark")
print(students)

# Add data before an specific index for example #2  "Ana Verónica" | HERE |  "David Alexander"
students.insert(2, "John")
print(students)

# Add Data to the end of the array
students.extend(["Andrew", "Tom", "Jerry"])
print(students)

# Add a new array
students2 = ["Jenny", "Jane", "Nicole"]
finalList = students+students2
print(finalList)

# Search something in an array > It returns true or false
print("Marco Antonio" in students) # True
print("Marcos" in students) # False

# Find the index for an item
print(students.index("Marco Antonio"))

# Find the times if it's repeating 
students.append("Marco Antonio")
print(students.count("Marco Antonio"))


# How to DELETE DATA
students.remove("Marco Antonio") # If there are 2 it will delete the first one
print(students)
students.extend([1,2,1,6,7,8,1,2])
element_to_remove = 1
# Deleting all the instances
while element_to_remove in students:
    students.remove(element_to_remove)
print(students)

# Making a reverse
students.reverse()
print(students)

# Delete the whole array
students.clear()
print(students) # It will print > []


numbers = [1,2,5,4,-50,100,25,-5,55]
numbers.sort() # Order from the minus to the max
print(numbers)
numbers.sort(reverse=True) # Order from the max to the minus
print(numbers)
