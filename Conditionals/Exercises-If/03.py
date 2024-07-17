name1 = input("Insert the first name: ")
name2 = input("Insert the second name: ")

#With index 0 "first letter", with - 1  "last letter"
if name1[0] == name2[0] or name1[-1] == name2[-1]:
    print(f"{name1} and {name2} have similitudes in the first letter or last letter")
else:
    print(f"{name1} and {name2} don't have similitudes in the first letter or last letter")