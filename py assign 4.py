
electricity_units = int(input("Enter electricity bill: "))


if electricity_units <= 100:
    print("Enter bill is", electricity_units * 0.5)
elif electricity_units <= 300 and electricity_units >= 101:
    print("Enter bill is", electricity_units * 0.75)
elif electricity_units > 300:
    print("bill is", electricity_units * 1)
