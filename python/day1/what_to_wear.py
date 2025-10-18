sicaklik = float(input("The temperature?: "))
if sicaklik > 25:
    print("You should wear shirt.")
elif sicaklik >= 15:
    print("You should wear jacket.")
elif sicaklik < 15:
    print("Palto giyebilirsiniz.")
else:
    print("Please make sure you entered a number.")