from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
to_continue = True
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
while to_continue:
    coffee_wanted = input(f"\nWhat coffee do you want? {menu.get_items()}: ").lower()
    coffee = menu.find_drink(coffee_wanted)
    if coffee_wanted == "off":
        to_continue = False
    elif coffee_wanted == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)




