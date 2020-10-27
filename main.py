from menus import menu
from standard import ask_yn, seperator

def display_menu():
    seperator(28)
    print(" " + "Name\t\t" + "Price")
    for entry in menu:
        print(" " + entry + "\t\t" + menu[entry])
    seperator(28)

def take_name(): # asks user for name. returns name if its valid
    n = ''
    while len(n) < 3:
        print("make sure the input is 3 or more characters long")
        n = input("What is your name? : ")
    return n

def take_phone(): # asks user for phone number, returns phone number if its valid
    while True:
        try:
            nb = int(input("what if your phone number? : "))
            return nb
        except ValueError:
            print("Make sure theres only numbers (0-9)")

def take_address(): # asks user for address, returns address if its valid
    i = 0
    x = 0
    while i < 1:
        try:
            street = str(input("Whats your street name?"))
            i = i + 123
        except ValueError:
            print("Make sure the name is entirely letters (a-z)")
    while x < 1:
        try:
            place = int(input("Whats your place on the street?"))
            x = x + 1134
        except ValueError:
            print("Make sure the place is entirely numbers (0-9)")

    return street + " " + str(place)

if ask_yn("Would you like to place an order?") == True:
    name = take_name()
    pnb = take_phone()
    address = take_address()

    display_menu()
    info = {"name" : name, "Phone number" : pnb, "address" : address}
    pending_order = {}
    pending = True

    while pending == True:
        selected_item = str(input("Select an item with its name ( f = finish ): "))
        if selected_item == "f":
            print(info)
            for entry in pending_order:
                eamount = pending_order[entry]["amount"]
                eprice = pending_order[entry]["price"]

                eamount = str(eamount)
                eprice = str(eprice)

                print(entry + "\t" + eamount + "\t" + menu[entry] + "\t" + eprice)
            
            v = 0
            for key in pending_order:
                v += pending_order[key]["price"]
            print(v)
                
        else:
            a = input("Add remove or change : ")
            if a == "add":
                amount = input("How much would you like to add : ")
                item = selected_item
                price = menu[selected_item]
                ffprice = float(price)
                ffamount = float(amount)
                fprice = ffprice * ffamount
                aaa = {"amount" : amount, "price" : fprice}
                pending_order[item] = aaa
                print(pending_order)
            elif a == "remove":
                item = selected_item
                del pending_order[item]
                print(pending_order)
            elif a == "change":
                amount = input("how much would you like to order instead: ")
                item = selected_item
                price = menu[selected_item]
                fprice = float(price)
                famount = float(amount)
                change = fprice * famount
                pending_order[item]["price"] = change
            else:
                print("false")