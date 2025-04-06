total = 0
for i in range(3):
    price = int(input(f"Enter price {i+1} "))
    total += price
    print("total amount is ", total)

if total >= 500:
    total = total * 10 / 100
    print("the total amount is ", total)
