list_products = ["Maxx", "Clover", "Safeguard", "Hansel", "Chippy"]
list_price = [1, 8, 15, 7, 40]

for x in range(5):
    print((x + 1), ".", list_products[x], "-", list_price[x])

print()
select = input("Select: ")

if select == "1":
    quantity = int(input("Quantity: "))
    total = price[0] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "2":
    quantity = int(input("Quantity: "))
    total = list_price[1] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "3":
    quantity = int(input("Quantity: "))
    total = list_price[2] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "4":
    quantity = int(input("Quantity: "))
    total = list_price[3] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "5":
    quantity = int(input("Quantity: "))
    total = list_price[4] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
else:
    print("Invalid choice")
