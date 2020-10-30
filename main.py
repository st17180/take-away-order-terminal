"""
Take away order cli.
Version 0.4
"""


menu = {
    "Fish": "2.40",
    "Chips": "2.40",
    "HotDog": "2.10",
    "Spring": "2.60",
    "Scallop": "1.60",
    "Donut": "2.00",
    "Egg": "2.30",
    "Burger": "4.10",
    "Sausage": "2.20",
    "Wedges": "4.00",
    "Chicken": "3.10",
    "Mince": "3.10"
}


# asks yes no. returns relating True/False
def ask_yn(question):
    a1 = False
    while a1 is False:
        a = input(question + "(y/n) : ")
        if a == "y":
            return True
        elif a == "n":
            return False
        else:
            print("make sure to awnser with only y or n")
            a1 = False


# Prints a visual seperator the length of {amount}
def seperator(amount):
    print("{" + "="*amount + "}")


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

# main loop. repeats upon order finish
while True:
    # greets the user
    seperator(53)
    print("Welcome to the Take away order terminal version")
    seperator(53)
    # ask user to start an order
    if ask_yn("Would you like to place an order?") is True:
        name = take_name()
        pnb = take_phone()
        address = take_address()
        display_menu()
        info = {"name": name, "Phone number": pnb, "address": address}
        pending_order = {}
        pending = True
        # menu selection loop
        while pending is True:
            selected_item = str(input("select an item by name\
                \n or f to finish  m to show menu  : "))
            # final selection loop
            if selected_item == "f":
                calc_order()
                a = input("cancel edit or finish the order? : ")
                # ends order editing
                if a == 'finish':
                    pending = False
                # clears pending order and resets
                elif a == 'cancell':
                    pending_order = {}
                    pending = False
                # returns to Editing
                elif a == 'edit':
                    pending = True
                # catches invalid input
                else:
                    print("make sure you entered finish cancel or edit")
            # displays menu 
            elif selected_item == "m":
                display_menu()
            # item selection and edit loop
            elif selected_item in menu:
                a = input("Add remove or change : ")
                # adds selected item to the order
                if a == "add" and selected_item not in pending_order:
                    try:
                        amount = int(input("amount to add : "))
                        # catches invalid input
                        if amount > 5 or amount < 1:
                            print("you can only have from 1 to 5")
                        # adds the amount of the selected item 
                        else:
                            item = selected_item
                            price = menu[selected_item]
                            ffprice = float(price)
                            ffamount = float(amount)
                            fprice = ffprice * ffamount
                            aaa = {"amount": amount, "price": fprice}
                            pending_order[item] = aaa
                            print(pending_order)
                    # catches invalid inputs
                    except ValueError:
                        print("Make sure input is only 0-9")
                # removes selected item from the order
                elif a == "remove" and selected_item in pending_order:
                    item = selected_item
                    del pending_order[item]
                    print(pending_order)
                # chnages the amount of an item in the order
                elif a == "change" and selected_item in pending_order:
                    try:
                        amount = int(input("amount to order : "))
                        # catches invalid input
                        if amount > 5 or amount < 1:
                            print("you can only have from 1 to 5")
                        # changes based on selection and amount
                        else:
                            item = selected_item
                            price = menu[selected_item]
                            fprice = float(price)
                            famount = float(amount)
                            change = fprice * famount
                            pending_order[item]["price"] = change
                            pending_order[item]["amount"] = amount
                            print(pending_order)
                    # catches invalid input
                    except ValueError:
                        print("Make sure input is only 0-9")
                # catches invalid inputs
                else:
                    print("Make sure the selected item in in the menu\
                    \n or when removing that it is in the order")
            # catches invalid inputs
            else:
                print('Make sure the name is the same as the menu. or "f" ')
        # displays final order and takes payment
        seperator(53)
        print("Your final order is")
        calc_order()
        print("continue at card reader")
        seperator(53)
    # resets ready to take another order
    else:
        print("Good bye!")
