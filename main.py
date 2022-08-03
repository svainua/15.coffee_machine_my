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

profit = 0
income = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def money():
    quarters = (int(input("How many quarters?: "))) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)

def report():
    """gives the info about availability of ingredients"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f" water: {water}ml\n milk: {milk}ml\n coffee: {coffee}g\n money: ${round(profit,2)} ")


def recipe(coffee_type):
    """takes the offer, checks resources, reduces resources"""
    water = MENU[coffee_type]["ingredients"]["water"]
    coffee = MENU[coffee_type]["ingredients"]["coffee"]
    if prompt != "espresso":
        milk = MENU[coffee_type]["ingredients"]["milk"]

    if resources["water"] < water:
        print("Sorry there is not enough water.")
    elif resources["coffee"] < coffee:
        print("Sorry there is not enough coffee.")
    elif coffee_type != "espresso" and resources["milk"] < milk:
        print("Sorry there is not enough milk.")
    else:
        resources["water"] -= water
        resources["coffee"] -= coffee
        if coffee_type != "espresso":
            resources["milk"] -= milk


def sale(coffee_type, profit):
    print("Please insert coins. ")
    income = money()
    profit = profit + income
    print(f"${profit}")
    if income < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        profit = profit - income
    elif income > MENU[coffee_type]["cost"]:
        change = round(income - MENU[coffee_type]["cost"], 2)
        recipe(coffee_type)
        print(f"Here is ${change} in change")
        print(f"Here is your {coffee_type}. Enjoy!")
        profit -= change
        return profit
        print(f' water: {resources["water"]}ml\n milk: {resources["milk"]}ml\n coffee: {resources["coffee"]}g\n money: ${round(profit, 2)}')

should_continue = True

while should_continue:
    prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    if prompt == "off":
        should_continue = False
    if prompt == "report":
        report()
    if prompt == "espresso":
        profit = sale("espresso", profit)
    if prompt == "latte":
        profit = sale("latte", profit)
    if prompt == "cappuccino":
        profit = sale("cappuccino", profit)





