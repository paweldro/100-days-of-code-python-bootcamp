from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

while True:
    user_choice = input(f"What would you like? ({menu.get_items()}):")
    if user_choice == "report":
        coffee.report()
        money.report()
        continue
    elif user_choice == "off":
        break
    elif menu.find_drink(user_choice) is not None:
        drink = menu.find_drink(user_choice)
    else:
        continue

    if money.make_payment(drink.cost) and coffee.is_resource_sufficient(drink):
        coffee.make_coffee(drink)
    else:
        continue


