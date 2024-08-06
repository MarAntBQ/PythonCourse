# Variables in python are case sensitive, so the variable name "name" is different from "Name", "NAME", "nAmE", etc.
# I can't use a number as the first character of a variable name, but I can use it in the middle or at the end.
# Also I can set as "_" the first character of a variable name, but it's not recommended.
# Also "var_name" is different from "varname" and "VarName".

# Examples
# full-name = "Marco Antonio Bustillos Quiroz" // It's not allowed
userName = "Marco Antonio"
firstname = "Marco"
second_name = "Antonio"
_lastName = "Bustillos"
SecondLastName = "Quiroz"

# print("Full Name:", full-name) SintaxError
print("Name:", userName)
print("First Name:", firstname)
print("Second Name:", second_name)
print("Last Name:", _lastName)
print("Second Last Name:", SecondLastName)

# class = "Python" // It's not allowed because "class" is a reserved word

