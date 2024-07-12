print('Welcome to MarAntBQ.dev Store')

vat = 15
discount = 36
subtotal = float(input(f"Please insert the value pre-tax to be discounted ({36}%): "))

calc_discount = subtotal * (discount/100)
print(calc_discount)
calc_vat = (subtotal - calc_discount) * (vat / 100)
print(calc_vat)
total = (subtotal - calc_discount) + calc_vat

print(total)