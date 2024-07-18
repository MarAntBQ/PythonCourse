balance = 2000
# ATM App

print("Welcome to MarAntBQ ATM")
print("Menu")
print("1.- Deposit Money")
print("2.- Withdraw Money")
print("3.- Balance")
print("4.- Exit")
userOption = int(input("\nChoose option: "))

if userOption == 1:
    ammount = float(input("Insert the money ammount: "))
    balance += ammount
    print(f"Your current balance is: ${balance}")
elif userOption == 2:
    ammount = float(input("Insert the money ammount: "))
    balance -= ammount
    print(f"Your current balance is: ${balance}")
elif userOption == 3:
    print(f"Your current balance is: ${balance}")
else:
    print("Exit")
