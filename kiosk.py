# Author : Erick Lanchipa
# Class : ITN160
# Class Section : 201
# Date : 03/27/2026
# Module 9 Project 2: Restaurant Kiosk


# 1. Show welcome and menu
print("Welcome to the Restaurant Kiosk and Menu!!!")
print("")

# 2. Create menu dictionary
menu = {

    1: ("Black Pearl Burger", 8.50),
    2: ("Kraken Bites", 6.00),
    3: ("Tortuga Punch Run (Non-Alcoholic)", 3.50),
    4: ("Jack's Fish Plate", 10.50),
    5: ("Treasure Salad", 5.50),
    6: ("Port Royal Chicken Wrap", 7.25),
    7: ("Davy Jones Clam Chowder", 4.75),
    8: ("Mermaid Lagoon Smoothie", 4.25),
    9: ("Barbossa's BBQ Ribs", 11.50),
    10: ("Gold Doubloon Cookie", 2.50)

}
# 3. Print the menu for the user
for number, (name, price) in menu.items():
    print(f"{number})  {name} - ${price:.2f}")

# 4. Create the list to store orders
orders = []

# 10. Create loop to allow multiple orders
while True:
    # 5. Ask for Menu Choice
    choice = int(input("\nEnter the item number you want to order (1-10): "))

    # 6. Check User Selection
    if choice in menu:
        print(f"You selected: {menu[choice][0]}")

        # 7. Ask for Quantity (with limit)
        quantity = int(input("How many would you like to order? "))
        while quantity < 1 or quantity > 100:
            print("Please enter a number between 1 and 100.")
            quantity = int(input("Please enter a valid quantity: "))

        # 8. Add the Item to Order List
        item_name, item_price = menu[choice]
        subtotal = item_price * quantity
        orders.append((item_name, item_price, quantity, subtotal))

        # 9. Ask if customer wants to order another item

        another = (input("Would you like to order another item? (Y/N): ").lower())

        if another not in ("y","yes"):
            break

    else:
         print("Invalid Choice. Please restart and enter a valid choice from the menu.")





# 11 Print the receipt
print("\n-------RECEIPT --------\n")

grand_total = 0

for name, price, qty, subtotal in orders:
    print(f"{name}  x{qty}  ${price:.2f} = ${subtotal:.2f}")
    grand_total += subtotal

print("\n--------------------------")
print(f"GRAND TOTAL: ${grand_total:.2f}")
print("\n--------------------------")