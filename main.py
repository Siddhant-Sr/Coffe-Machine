from data import MENU, resources, profit


def coffee_details(coffee):
    for items in coffee:
        if coffee[items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True



def money():
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickles + pennies

def money_processing(drink_cost, money):
    if money == drink_cost:
        global profit
        profit += money
        return True
    elif money > drink_cost:
        print(f"Here is your change {money - drink_cost}")
        profit += (money - drink_cost)
        return True
    else:
        print(f"Money is not sufficient")
        return False


def report():
    print(f'''
    Water = {resources['water']}ml
    Milk = {resources['milk']}ml
    Coffee = {resources['coffee']}
    Money = {profit}''')

def make_coffee(drink_name, ingredients):
    for items in ingredients:
        resources[items] -= ingredients[items]
    print(f"Here is your  {drink_name}")

is_on = True

while is_on:
    order = input("What would you like to have? ('espresso','latte', 'cappuccino'): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        report()
    else:
        drink = MENU[order]
        if coffee_details(drink['ingredients']):
            total = money()

            if money_processing(drink['cost'] , total):
                make_coffee(order, drink['ingredients'])










