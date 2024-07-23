n1 = int(input("Enter the first numer: "))
n2 = int(input("Enter the second numer: "))
n3 = int(input("Enter the third numer: "))


if n1>=n2 and n1>=n3:
    print(f"{n1} is the max number")
elif n2>=n1 and n2>=n3:
    print(f"{n2} is the max number")
elif n3>=n1 and n3>=n2:
    print(f"{n3} is the max number")
