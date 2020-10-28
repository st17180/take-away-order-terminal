# imports menu and extra functions from menu.py and standard.py
from menus import menu
from standard import ask_yn, seperator
"""
Take away order cli.
"""
version = " beta : 0.3"


# Displays menu dictionary in a styled way
def display_menu():
    seperator(28)
    print(" Name\t\tPrice")
    for entry in menu:
        print(" " + entry + "\t\t" + menu[entry])
    seperator(28)


# handles taking users name and out of bound entrys
def take_name():
    x = True
    while x:
        name = input("What is your name? : ")
        if name == '':
            print("please enter a valid input")
        elif all(x.isalpha() or x.isspace() for x in name):
            x = False
            return name
        else:
            print("Make sure input is valid")


# handles taking users phone number and out of bound entrys
def take_phone():
    while True:
        try:
            nb = int(input("what if your phone number? (0-9) : "))
            while len(str(nb)) > 15:
                print("Make sure the number is not over 15 characters long")
                nb = int(input("what is your phone number? (0-9) : "))
            return nb
        except ValueError:
            print("Make sure theres only numbers (0-9) and input is not empty")


# handles taking users address street/place and out of bound entrys
def take_address():
    i = True
    x = True
    while i is True:
        try:
            street = str(input("Whats your street name? : "))
            if street == '':
                print("Make sure its not empty")
            else:
                i = False
        except ValueError:
            print("Make sure the name is entirely letters (a-z)")
    while x is True:
        try:
            place = int(input("Whats your place on the street? : "))
            x = False
        except ValueError:
            print("Make sure the place is entirely numbers (0-9)")

    return street + " " + str(place)


# calculates and displays the users current order if a styled way
def calc_order():
    user_info = 'Name : ' + name +\
                ' | Phone number : ' + str(pnb) +\
                ' | address : ' + address
    print(user_info)
    print("name\tamount\tprice per item\ttotal amount price")
    for entry in pending_order:
        eamount = pending_order[entry]["amount"]
        eprice = pending_order[entry]["price"]

        eamount = str(eamount)
        eprice = str(eprice)
        print(entry + "\t" + eamount + "\t" + menu[entry] + "\t\t" + eprice)

    v = 0
    for key in pending_order:
        v += pending_order[key]["price"]
        print("Total price : " + str(v))

while True:
    seperator(53)
    print("Welcome to the Take away order terminal version : " + version)
    seperator(53)
    if ask_yn("Would you like to place an order?") is True:
        name = take_name()
        pnb = take_phone()
        address = take_address()

        display_menu()
        info = {"name": name, "Phone number": pnb, "address": address}
        pending_order = {}
        pending = True

        while pending is True:
            selected_item = str(input("select an item by name or\
                f to finish / m to show menu  : "))
            if selected_item == "f":
                calc_order()
                a = input("cancel edit or finish the order? : ")
                if a == 'finish':
                    pending = False
                elif a == 'cancell':
                    pending_order = {}
                    pending = False
                elif a == 'edit':
                    pending = True
                else:
                    print("make sure you entered finish cancel or edit")
            elif selected_item == "m":
                display_menu()
            elif selected_item in menu:
                a = input("Add remove or change : ")
                if a == "add" and selected_item not in pending_order:
                    try:
                        amount = int(input("amount to add : "))
                        if amount > 5 or amount < 1:
                            print("you can only have from 1 to 5")
                        else:
                            item = selected_item
                            price = menu[selected_item]
                            ffprice = float(price)
                            ffamount = float(amount)
                            fprice = ffprice * ffamount
                            aaa = {"amount": amount, "price": fprice}
                            pending_order[item] = aaa
                            print(pending_order)
                    except ValueError:
                        print("Make sure input is only 0-9")
                elif a == "remove" and selected_item in pending_order:
                    item = selected_item
                    del pending_order[item]
                    print(pending_order)
                elif a == "change" and selected_item in pending_order:
                    try:
                        amount = int(input("amount to order : "))
                        if amount > 5 or amount < 1:
                            print("you can only have from 1 to 5")
                        else:
                            item = selected_item
                            price = menu[selected_item]
                            fprice = float(price)
                            famount = float(amount)
                            change = fprice * famount
                            pending_order[item]["price"] = change
                            pending_order[item]["amount"] = amount
                            print(pending_order)
                    except ValueError:
                        print("Make sure input is only 0-9")
                else:
                    print("Make sure the selected item in in the menu \
                    or if removing or chaning that the item is in your \
                    order before changing or removing. ")
            else:
                print('Make sure the name is the same as the menu. or "f" ')
        seperator(53)
        print("Your final order is")
        calc_order()
    else:
        print("Good bye!")
