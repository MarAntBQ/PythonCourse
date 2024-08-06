print("Welcome to the Hotel Booking App!")

reservations = ["Marco Antonio", 28, 5, 101], ["Juan Perez", 35, 3, 102], ["Maria Lopez", 40, 2, 103]
dailyRate = 100

for guest in reservations:
    print(f"--------------------------\nName: {guest[0]}\nAge: {guest[1]}\nDays: {guest[2]}\nRoom: {guest[3]}\nDaily Rate: ${float(guest[2]*dailyRate)} \n--------------------------")