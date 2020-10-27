# asks a yes no question. returns true if awnsered yes returns False if awnsered no
def ask_yn(question):
    a1 = False
    while a1 == False:
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
    print("{", end = '')
    while amount > 0:
        print("=", end = '')
        amount = amount - 1
    print("}")