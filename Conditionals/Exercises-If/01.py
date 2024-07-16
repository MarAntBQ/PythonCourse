num1 = int(input("Please insert number 1: "))
num2 = int(input("Please insert number 2: "))

if num1%2==0 and num2%2==0:
    print(f"{num1} & {num2} are pairs")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} is pair")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} is pair")
else:
    print("You did not enter a pair number")