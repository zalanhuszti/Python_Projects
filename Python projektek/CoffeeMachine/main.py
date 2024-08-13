MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}

QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNY = 0.01

# TODO: Prompting user by asking “What would you like? (espresso/latte/cappuccino):”


def choosing_coffee(choice):

    if choice == "espresso":
        coffee = MENU[choice]
    elif choice == "latte":
        coffee = MENU[choice]
    elif choice == "cappuccino":
        coffee = MENU[choice]

    return coffee


# TODO: Printing report
def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")

# TODO: Checking resources whether it is sufficient or not


def check_resources(coffee, resources):
    is_resources_enough = True
    for ingredient in coffee["ingredients"]:
        if coffee["ingredients"][ingredient] <= resources[ingredient]:
            continue
        else:
            is_resources_enough = False
            print(f"Sorry, there is not enough {ingredient}.")
            break

    return is_resources_enough

# TODO: Processing coins


def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_money = quarters * QUARTER + dimes * DIME + nickles * NICKLE + pennies * PENNY
    return round(total_money, 2)

# TODO: Checking transaction


def check_transaction(money_added, cost_of_coffee):

    if money_added >= cost_of_coffee:
        change = round(money_added - cost_of_coffee, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def making_coffee(coffee, resources):
    for ingredient in resources:
        if ingredient != "money":
            resources[ingredient] -= coffee["ingredients"][ingredient]
        else:
            resources[ingredient] += coffee["cost"]

    return resources


turned_on = True

while turned_on:
    decision = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: Turning off the Coffee Machine by entering “off” to the prompt
    if decision == "off":
        turned_on = False
        break
    elif decision == "report":
        print_report()
    else:
        chosen_coffee = choosing_coffee(decision)
        if check_resources(chosen_coffee, resources):
            money_added = process_coins()
            if check_transaction(money_added, chosen_coffee["cost"]):
                resources = making_coffee(chosen_coffee, resources)
                print(f"Here is your {decision}☕. Enjoy!")

            else:
                continue
