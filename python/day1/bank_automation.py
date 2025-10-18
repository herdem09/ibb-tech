money_amount = 500
money_wanted_get = float(input("Please enter how much of maney you want to get: "))
if 0 < money_wanted_get <= money_amount:
    print(f"You will have your {money_wanted_get}")
elif money_wanted_get > 500:
    print(f"You can not get this much of money. Money amount: {money_amount}.")
elif money_wanted_get < 0:
    print(f"You can not get -money???. Money amount{money_amount}.")
else:
    print("Please make sure you entered number.")