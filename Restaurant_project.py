#Define Menu
menu_item = {
    '1' : 'Pizza',
    '2' : 'Burger',
    '3' : 'Pasta'
}
menu_price = {
    'Pizza' :50,
    'Burger' :30,
    'Pasta' :40
}

#Welcome note
print("Welcome to the Restaurant")
print("-----MENU-----")
print("1. Pizza : Rs. 50\n2. Burger : Rs. 30\n3. Pasta : Rs. 40")

order_item = 0

order_total = 0

item1 = input("Enter the Item : ")
if item1 in menu_item:
    order_item = menu_item.get(item1)
    order_total += menu_price.get(order_item)
    print(f"Your item {order_item} is added")
    print(f"Your order value is {order_total}")
    ask_another_item = input("Do you want to add another item? (Yes/No): ")
    if ask_another_item == "Yes" or ask_another_item == "yes" or ask_another_item == "YES":
        item2 = input("Enter the item: ")
        if item2 in menu_item:
            order_item = menu_item.get(item2)
            order_total += menu_price.get(order_item)
            print(f"Your item {order_item} is added.")
            print(f"Your order value is {order_total}.")
        else:
            print("Please recheck your order")
    else:
        print("Thankyou for Ordering! Dont forget to visit us again")
        print(f"Your Total Bill: {order_total}")
else:
    print("Please recheck your order")

