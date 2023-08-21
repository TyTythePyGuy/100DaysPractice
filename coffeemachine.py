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
# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
running = True
while running:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 3. Print report
    if drink_choice == 'report':
        for values in resources:
            print(values.title(), ":", resources[values])
    # TODO: 2. Create an off input by entering 'off'
    elif drink_choice == 'off':
        running = False
    # TODO: 4. Check resources sufficient?
    elif drink_choice == 'espresso':
        if (MENU["espresso"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"][
                "coffee"] <= resources["coffee"]):
            print("Please insert coins")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_money = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
            if total_money >= MENU["espresso"]["cost"]:
                total_money -= MENU["espresso"]["cost"]
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print(f"Here is your ${round(total_money, 2)} in change.")
                print(f"Here is your {drink_choice} ☕. Enjoy!")
                total_money = 0
            elif total_money < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                total_money = 0
        elif MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water")
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee")
    elif drink_choice == 'latte':
        if (MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["latte"]["ingredients"][
                "coffee"] <= resources["coffee"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"]):
            print("Please insert coins")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_money = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
            if total_money >= MENU["latte"]["cost"]:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                print(f"Here is your ${round(total_money, 2)} in change.")
                print(f"Here is your {drink_choice} ☕. Enjoy!")
                total_money = 0
            elif total_money < MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                total_money = 0
        elif MENU["latte"]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water")
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee")
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there is not enough milk")
    elif drink_choice == 'cappuccino':
        if (MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and MENU["cappuccino"]["ingredients"][
                "coffee"] <= resources["coffee"] and MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]):
            print("Please insert coins")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_money = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
            if total_money >= MENU["cappuccino"]["cost"]:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                print(f"Here is your ${round(total_money, 2)} in change.")
                print(f"Here is your {drink_choice} ☕. Enjoy!")
                total_money = 0
            elif total_money < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                total_money = 0
        elif MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water")
        elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee")
        elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there is not enough milk")
    else:
        print("Yea.....we don't sell that here....")
