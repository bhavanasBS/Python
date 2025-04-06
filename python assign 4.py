def balance(bal, limit, withdraw):
    if (bal > limit and (bal - withdraw) > limit):
        bal -= withdraw
        print(bal)
    else:
        print("Insufficient balance cannot withdraw")

balance(500, 200, 400)
