"""
Coffee Machine

Description:
This Python project simulates the operation of a coffee vending machine. The program allows users to select drinks, manage ingredient levels, and process payments in euros. It includes features such as:

Interactive menu for selecting coffee types (Espresso, Latte, Cappuccino).
Real-time tracking of ingredient levels (water, milk, coffee, and sugar) in the machine’s reservoir.
Coin-based payment processing with proper calculation of total payment and change returned.
Automatic validation of available ingredients before serving drinks, ensuring proper resource management.
Machine state updates after each transaction, including total revenue and drinks served.
A final machine report displaying the current status of resources, total earnings, and sales statistics upon shutdown.

"""
# Dictionary representing the coffee machine menu
coffee_menu = {
    "espresso": {
        "ingredients": {
            "water": 50,   # in milliliters
            "coffee": 18   # in grams
        },
        "cost": 1.5      # cost in euros
    },
    "latte": {
        "ingredients": {
            "water": 200,  # in milliliters
            "milk": 150,   # in milliliters
            "coffee": 24   # in grams
        },
        "cost": 2.5      # cost in euros
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,  # in milliliters
            "milk": 100,   # in milliliters
            "coffee": 24   # in grams
        },
        "cost": 3.0      # cost in euros
    }
}

# Dictionary representing the coffee machine's reservoir
reservoir = {
    "water": {"capacity": 2000, "current_level": 2000, "unit": "ml"},
    "milk": {"capacity": 1000, "current_level": 1000, "unit": "ml"},
    "coffee": {"capacity": 500, "current_level": 500, "unit": "grams"},
    "sugar": {"capacity": 300, "current_level": 300, "unit": "grams"}
}

euro_currency = {
    'one_cent': 0.01,
    'two_cents': 0.02,
    'five_cents': 0.05,
    'ten_cents': 0.1,
    'twenty_cents': 0.2,
    'fifty_cents': 0.5,
    'one_euro': 1,
    'two_euro': 2
}

machine_state = {
    "money": 0.0,
    "drinks_served": {
        "espresso": 0,
        "latte": 0,
        "cappuccino": 0
    }
}


def get_user_choice():
    """Presents and returns the user options"""

    print("---------------------")
    print("What would you like today?")
    print("---------------------")

    choice = input("\n[C]offee Menu\n[R]eservoir\n[O]ff\n").lower().strip()
    if choice not in ['c', 'r', 'o']:
        print("Invalid input. Please, choose a valid option")
        return get_user_choice()
    return choice


def get_machine_menus(user_choice):
    """Retrieves and displays the menus based on the user's choice"""
    if user_choice == 'c':
        drinks = list(coffee_menu.keys())
        # formated and numbered string of the drinks
        options_str = "\n".join(f"{index + 1}. {drink.title()}" for index, drink in enumerate(drinks))
        print(f"Drinks: \n{options_str}")
        return drinks
    
    elif user_choice == 'r':
        # show the current levels of the reservoir
        reservoir_status  = "\n".join(
            f"{ingredient.title()}: {detail['current_level']}/{detail['capacity']} {detail['unit']}" for ingredient, detail in reservoir.items()
        )
        print(f"Reservoir Status: {reservoir_status}")
        return reservoir_status
    else:
        # Show power off option
        state_on = False
        print("Turning off the machine...")
        return state_on


def get_drink_cost(drinks):
    """
    Prompts the user to choose a drink by number, retrieves its cost from the coffee_menu
    and returns the cost
    """
    try:
        drink_choice = int(input("Select your drink: "))
        if drink_choice < 1 or drink_choice > len(drinks):
            print("Invalid choice. Plese try again.")
            return get_drink_cost(drinks)
    except ValueError:
        print("Invalid input. Pleae enter valid number.")
        return get_drink_cost(drinks)
    
    selected_drink = drinks[drink_choice - 1]
    selected_drink_cost = coffee_menu[selected_drink]['cost']

    print(f"The cost of {selected_drink.title()} is €{selected_drink_cost:.2f}.")
    return selected_drink, selected_drink_cost
    

def get_payment():
    """
    Promps the user for the number of coins inserted for each currency and calculate the total payment in euros
    """
    try:
        one_cent = int(input("Enter the number of -- 1 cent -- coins: "))
        two_cents = int(input("Enter the number of -- 2 cent -- coins: "))
        five_cents = int(input("Enter the number of -- 5 cent -- coins: "))
        ten_cents = int(input("Enter the number of -- 10 cent -- coins: "))
        twenty_cents = int(input("Enter the number of -- 20 cent -- coins: "))
        fifty_cents = int(input("Enter the number of -- 50 cent -- coins: "))
        one_euro = int(input("Enter the number of -- 1 euro -- coins: "))
        two_euros = int(input("Enter the number of -- 2 euro -- coins: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return get_payment()
   
    total_inserted = (
        one_cent * euro_currency['one_cent'] +
        two_cents * euro_currency['two_cents'] +
        five_cents * euro_currency['five_cents'] +
        ten_cents * euro_currency['ten_cents'] +
        twenty_cents * euro_currency['twenty_cents'] +
        fifty_cents * euro_currency['fifty_cents'] +
        one_euro * euro_currency['one_euro'] +
        two_euros * euro_currency['two_euro']
    )
    return total_inserted


def get_change(selected_drink_cost, total_inserted):
    change = total_inserted - selected_drink_cost
    if change < 0:
        print(f"Insufficient funds. Saldo: €{change}")
        return get_change(selected_drink_cost, total_inserted)
    else:
        print(f"Change: €{change}\nThank you! Enjoy!")


def check_and_update_reservoir(reservoir, drink):
    """
    Updates the reservoir by subtracting the ingredients required fot the selected drink.
    Parameters:
        Reservoir (dict): the current amounts of ingredients
        Drink (str): the name of the drink (e.g., "espresso")
    return:
        Bool:
            True: there are enough ingredients and can make the drink
            False: not enough ingredients and cannot make the drink
    """
    required_ingredients = coffee_menu[drink]["ingredients"]

    for ingredient, required_amount in required_ingredients.items():
        if ingredient not in reservoir:
            print(f"Error: {ingredient} is not available in the reservoir.")
            return False
        if reservoir[ingredient]["current_level"] < required_amount:
            print(f"Insufficient {ingredient} to serve {drink.title()}.")
            return False
        
    for ingredient, required_amount in required_ingredients.items():
        reservoir[ingredient]["current_level"] -= required_amount

    print(f"{drink.title()} is served!")
    return True

def print_report():
    """
    Prints the report:
        - Reservoir: current level
        - Money: total amount collected
        - Drinks: amount of drinks served for each drink
    """

    print("===== MACHINE REPORT =====\n")

    print("Reservoir Levels: ")

    for ingredient, details in reservoir.items():
        current = details["current_level"]
        capacity = details["capacity"]
        unit = details["unit"]
        percentage = (current / capacity) * 100
        print(f"> {ingredient.title()} : {current}/{capacity} {unit} ({percentage:.1f}%)")

    print(f"\nMoney in machine: €{machine_state['money']:.2f}")

    print("\nDrinks Served:")
    for drink, count in machine_state["drinks_served"].items():
        print(f"{drink.title()}: {count}")


def update_machine_state(drink):
    """
    Updates the machine state after a drink is served.
    Parameters:
        drink (str): the name of the drink
    Actions:
        - Adds the cost to the total money collected
        - Increments the count for the served drink
    """

    cost = coffee_menu[drink]["cost"]
    machine_state["money"] += cost
    machine_state["drinks_served"][drink] += 1



# Main flow
while True:
    choice = get_user_choice()

    if choice == 'c':
        drinks = get_machine_menus(choice)
        selected_drink, drink_cost = get_drink_cost(drinks)
        total_payment = get_payment()
        get_change(drink_cost, total_payment)
        if check_and_update_reservoir(reservoir, selected_drink):
            update_machine_state(selected_drink)
    elif choice == 'r':
        get_machine_menus(choice)
    elif choice == 'o':
        print("Machine is turning off...")
        print_report()
        break






    



