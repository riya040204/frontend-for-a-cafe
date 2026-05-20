#Define the menue of the restaurant
menue = {
    'Pizza': 70,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 60,
    'Coffee': 80,
}

print("Welcome to our Python restaurant! Here is our menu:")
print("Pizza: Rs. 70 \nPasta: Rs. 50 \nBurger: Rs. 60 \nSalad: Rs. 60 \nCoffee: Rs. 80 ")

order_total = 0

item_1 = input("Please enter the first item you would like to order: ")
if item_1 in menue:
    order_total += menue[item_1]
else:
    print(f"Sorry, we do not have {item_1} on our menu.")

another_order = input("Would you like to order another item? (yes/no) ")
if another_order.lower() == 'yes':
    item_2 = input("Please enter the second item you would like to order: ")
    if item_2 in menue:
        order_total += menue[item_2]
    else:
        print(f"Sorry, we do not have {item_2} on our menu.")


print(f"Your total order amount is: Rs. {order_total}")               