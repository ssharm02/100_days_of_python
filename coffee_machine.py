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

total = 0


def user_coffee():
    users_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    return users_coffee


def pick_coffee():
    prompt_user = True
    while prompt_user:
        coffee_picked = user_coffee()
        user_selection = {}
        if coffee_picked == "espresso":
            user_selection = MENU[coffee_picked]
            compute_money(user_selection, coffee_picked)
        elif coffee_picked == "latte":
            user_selection = MENU["latte"]
            compute_money(user_selection, coffee_picked)
        elif coffee_picked == "cappuccino":
            user_selection = MENU["cappuccino"]
            compute_money(user_selection, coffee_picked)
        elif coffee_picked == "report":
            print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}ml\nMoney: ${resources["money"]}')
        elif coffee_picked == "off":
            print("Turning off coffee machine")
            prompt_user = False
            return
        else:
            print("Sorry you have made a bad selection")
        # Todo placing a return statement will defeat the while loop
        # return user_selection


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    users_total_dollar = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
    # print("user total dollars are ", round(users_total_dollar, 2))
    return users_total_dollar


def compute_money(user_selection, coffee_selection):
    final_coffee_selection = coffee_selection
    copy_user_selection = user_selection
    user_coffee_cost = user_selection["cost"]
    # Dollars paid by the user
    user_dollars = process_coins()
    can_user_afford = round(user_dollars - user_coffee_cost, 2)
    can_user_afford_coffee(calculated_total=can_user_afford, user_total=user_dollars, user_input=copy_user_selection, coffee_selection = final_coffee_selection)


def compute_resources(user_selection):
    user_ingredient_cost = user_selection["ingredients"]
    global resources
    resources = {key: resources[key] - user_ingredient_cost.get(key, 0) for key in resources}
    check_resources(resources)


def can_user_afford_coffee(calculated_total, user_total, user_input, coffee_selection):
    if calculated_total >= 0:
        resources["money"] = calculated_total
        print(f"Here is ${calculated_total} in change.")
        print(f"Here is you {coffee_selection}!  Enjoy ^_^!")
        compute_resources(user_input)
    else:
        global total
        total += user_total
        resources["money"] = total
        print("Sorry that's not enough money. Money Refunded.")
        return


def serve_drinks():
    print("running serving drinks function")


# Method checks if any of keys in resources are empty
def check_resources(updated_resources):
    for key, value in updated_resources.items():
        if value <= 0:
            print(f"Sorry that's not enough {key}.")
            return


resources["money"] = 0
pick_coffee()

