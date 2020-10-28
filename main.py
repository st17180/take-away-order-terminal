from menus import menu
from standard import ask_yn, seperator
"""
Take away order cli.
"""
version = " beta : 0.2"

def display_menu():
    seperator(28)
    print(" Name\t\tPrice")
    for entry in menu:
        print(" " + entry + "\t\t" + menu[entry])
    seperator(28)

def take_name(): # asks user for name. returns name if its valid
    x = True
    while x:
        name = input("What is your name? : ")
        if name == '':
            print("please enter a valid input")
        elif all(x.isalpha() or x,isspace() for x in name):
            x = False
            return name
        else:
            print("Make sure input is valid")

def take_phone(): # asks user for phone number, returns phone number if its valid
    while True:
        try:
            nb = int(input("what if your phone number? (0-9) : "))
            while len(str(nb)) > 15:
                print("Make sure the number is not over 15 characters long")
                nb = int(input("what is your phone number? (0-9) : "))
            return nb
        except ValueError:
            print("Make sure theres only numbers (0-9) and input is not empty")

def take_address(): # asks user for address, returns address if its valid
    i = True
    x = True
    while i == True:
        try:
            street = str(input("Whats your street name? : "))
            i = False
        except ValueError:
            print("Make sure the name is entirely letters (a-z)")
    while x == True:
        try:
            place = int(input("Whats your place on the street? : "))
            x = False
        except ValueError:
            print("Make sure the place is entirely numbers (0-9)")

    return street + " " + str(place)

def calc_order():
    print("name : " + name + " | Phone number : " + str(pnb) + " | address : " + address)
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
    if ask_yn("Would you like to place an order?") == True:
        name = take_name()
        pnb = take_phone()
        address = take_address()

        display_menu()
        info = {"name" : name, "Phone number" : pnb, "address" : address}
        pending_order = {}
        pending = True

        while pending == True:
            selected_item = str(input("Select an item with its name or f to finish : "))
            if selected_item == "f":
                calc_order()
                if ask_yn("Would you like to edit your order?") == False:
                    pending = False
                else:
                    pending = True
            elif selected_item in menu:
                a = input("Add remove or change : ")
                if a == "add" and not selected_item in pending_order:
                    try:
                        amount = int(input("How much would you like to add : "))
                        if amount > 5 or amount < 1:
                            print("you can only have from 1 to 5")
                        else:
                            item = selected_item
                            price = menu[selected_item]
                            ffprice = float(price)
                            ffamount = float(amount)
                            fprice = ffprice * ffamount
                            aaa = {"amount" : amount, "price" : fprice}
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
                        amount = input("how much would you like to order instead: ") # make sure amount is 5 or less and only 0-9 and not empty
                        if amount  > 5 or amount < 1:
                            print("you can only have from 1 to 5")
                        else:
                            item = selected_item
                            price = menu[selected_item]
                            fprice = float(price)
                            famount = float(amount)
                            change = fprice * famount
                            pending_order[item]["price"] = change
                            print(pending_order)
                    except ValueError:
                        print("Make sure input is only 0-9")
                else:
                    print("Make sure the selected item in in the menu or if removing or chaning that the item is in your order before changing or removing. ")
            else:
                print('Make sure the name is the same as the menu. or "f" ')
        seperator(53)
        print("Your final order is")
        calc_order()
    else:
        print("idek")