MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def prompt_user():
    user_choice = input("What would you like? (espresso/latte/cappuccino):")

    if user_choice == "off":
        pass

    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif user_choice not in MENU.keys():
        print(f"{user_choice} coffee dont exist")
        user_choice = "error"

    else:
        pass

    return user_choice


def check_resources(user_choice):
    for key in MENU[user_choice]["ingredients"].keys():
        if MENU[user_choice]["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return True
    return False


def process_coins(user_choice, profit):
    quarters = input("How much quarters:")
    while not quarters.isnumeric():
        print("That is not a quarters, enter again.")
        quarters = input("How much quarters:")

    dimes = input("How much dimes:")
    while not dimes.isnumeric():
        print("That is not a dimes, enter again.")
        dimes = input("How much dimes:")


    nickles = input("How much nickles:")
    while not nickles.isnumeric():
        print("That is not a nickles, enter again.")
        nickles = input("How much nickles:")

    pennies = input("How much pennies:")
    while not pennies.isnumeric():
        print("That is not a pennies, enter again.")
        pennies = input("How much pennies:")

    money_value = float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickles) * 0.05 + float(pennies) * 0.01
    if money_value < MENU[user_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return -1
    else:
        change = money_value - MENU[user_choice]["cost"]
        if change != 0:
            print(f"Here is ${round(change, 2)} dollars in change")
        profit = profit + MENU[user_choice]["cost"]
    return profit


def make_coffe(user_choice):
    for key in MENU[user_choice]["ingredients"].keys():
        resources[key] = resources[key] - MENU[user_choice]["ingredients"][key]
    print(f"Here is your {user_choice}. Enjoy!")


while True:
    user_choice = prompt_user()

    if user_choice == "report":
        continue
    elif user_choice == "off":
        break
    elif user_choice == "error":
        continue
    else:
        pass

    if check_resources(user_choice) == 0:
        pass
    else:
        continue
    if process_coins(user_choice, profit) == -1:
        continue
    else:
        pass

    make_coffe(user_choice)

