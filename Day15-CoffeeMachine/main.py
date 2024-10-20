from data import MENU, resources


def make_coffee(coffee_type, available_resources):
    print("Here's your coffee. Enjoy!\n")
    available_resources1 = available_resources
    available_resources1["water"] -= MENU[coffee_type]["ingredients"]["water"]
    available_resources1["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    available_resources1["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    return available_resources1


def ingredients_check(coffee_type, available_resources):
    """Returns a list of ingredients that aren't sufficient"""
    not_available = []
    if available_resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        not_available.append("Water")
    if available_resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        not_available.append("Milk")
    if available_resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        not_available.append("Coffee")
    return not_available


def take_money(coffee_type, available_resources):
    cost = MENU[coffee_type]["cost"]
    print(f"{coffee_type.capitalize()} costs ${cost} Enter the coins")
    pennies = int(input("Pennies: "))
    nickels = int(input("Nickel: "))
    dimes = int(input("Dimes: "))
    quarters = int(input("Quarters: "))
    total_money_entered = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25)
    if total_money_entered >= cost:
        available_resources["register"] += cost
        return total_money_entered - cost
    else:
        return -1


def report(available_resources):
    print("Following are the reports")
    for item in available_resources:
        if item == "coffee":
            print(f"{item.capitalize()} : {available_resources[item]} gms")
        elif item == "register":
            print(f"{item.capitalize()} : ${available_resources[item]}")
        else:
            print(f"{item.capitalize()} : {available_resources[item]} ml")
    print("\n")


current_resources = resources
to_continue = True
while to_continue:
    coffee_wanted = input("What coffee do you want? 'Espresso', 'Latte' or 'Capuccino' : ").lower()
    if coffee_wanted == "off":
        to_continue = False
    elif coffee_wanted == "report":
        report(current_resources)
    else:
        unavailable = ingredients_check(coffee_wanted, current_resources)
        if len(unavailable) != 0:
            print("\nSorry, we're out of: ")
            for item in unavailable:
                print(item)
            print("\n")
        else:
            money_to_be_returned = take_money(coffee_wanted, current_resources)
            if money_to_be_returned == -1:
                print("\nSorry, that's not enough. Here's your refund\n")
            else:
                print(f"\nHere's your change ${money_to_be_returned}")
                current_resources = make_coffee(coffee_wanted, current_resources)






