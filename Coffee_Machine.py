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
class CoffeeMachine:
    def __init__(self):
        # Menu of coffee drinks
        self.coffee_menu = {
            "espresso": {
                "ingredients": {"water": 50, "coffee": 18},
                "cost": 1.5
            },
            "latte": {
                "ingredients": {"water": 200, "milk": 150, "coffee": 24},
                "cost": 2.5
            },
            "cappuccino": {
                "ingredients": {"water": 250, "milk": 100, "coffee": 24},
                "cost": 3.0
            }
        }

        # Reservoir status
        self.reservoir = {
            "water": {"capacity": 2000, "current_level": 2000, "unit": "ml"},
            "milk": {"capacity": 1000, "current_level": 1000, "unit": "ml"},
            "coffee": {"capacity": 500, "current_level": 500, "unit": "grams"},
            "sugar": {"capacity": 300, "current_level": 300, "unit": "grams"}
        }

        # Euro currency denominations
        self.euro_currency = {
            'one_cent': 0.01,
            'two_cents': 0.02,
            'five_cents': 0.05,
            'ten_cents': 0.1,
            'twenty_cents': 0.2,
            'fifty_cents': 0.5,
            'one_euro': 1,
            'two_euro': 2
        }

        # State of the machine
        self.machine_state = {
            "money": 0.0,
            "drinks_served": {
                "espresso": 0,
                "latte": 0,
                "cappuccino": 0
            }
        }

        # Machine power flag
        self.is_on = True

    def run(self):
        """
        Main loop for the CoffeeMachine.
        Continues until the user chooses to turn off the machine.
        """
        while self.is_on:
            choice = self._get_user_choice()

            if choice == 'c':
                drinks = self._get_machine_menus('c')  # Display coffee menu
                if drinks:  # If valid drinks retrieved
                    selected_drink, drink_cost = self._get_drink_cost(drinks)
                    total_inserted = self._get_payment()
                    self._get_change(drink_cost, total_inserted)

                    # Check if we can actually serve the drink
                    if self._check_and_update_reservoir(selected_drink):
                        self._update_machine_state(selected_drink)

            elif choice == 'r':
                # Reservoir report
                self._get_machine_menus('r')

            elif choice == 'o':
                # Turn off the machine
                self.is_on = False
                print("Machine is turning off...")
                self._print_report()
            else:
                # Fallback for invalid choice handling
                print("Invalid input. Please try again.")

    # -------------------------
    #    PRIVATE METHODS
    # -------------------------

    def _get_user_choice(self):
        """
        Presents and returns the user options: [C]offee Menu, [R]eservoir, [O]ff
        """
        print("---------------------")
        print("What would you like today?")
        print("---------------------")

        choice = input("\n[C]offee Menu\n[R]eservoir\n[O]ff\n").lower().strip()
        if choice not in ['c', 'r', 'o']:
            print("Invalid input. Please, choose a valid option.")
            return self._get_user_choice()
        return choice

    def _get_machine_menus(self, user_choice):
        """Retrieves and displays the menus based on the user's choice"""
        if user_choice == 'c':
            drinks = list(self.coffee_menu.keys())
            options_str = "\n".join(f"{index + 1}. {drink.title()}"
                                    for index, drink in enumerate(drinks))
            print(f"Drinks: \n{options_str}\n")
            return drinks

        elif user_choice == 'r':
            # Show the current levels of the reservoir
            reservoir_status = "\n".join(
                f"{ingredient.title()}: {detail['current_level']}/{detail['capacity']} {detail['unit']}"
                for ingredient, detail in self.reservoir.items()
            )
            print(f"Reservoir Status: \n{reservoir_status}\n")
            return reservoir_status

        else:
            # Optionally handle other menus
            return None

    def _get_drink_cost(self, drinks):
        """
        Prompts the user to choose a drink by number, retrieves its cost, returns drink name & cost.
        """
        try:
            drink_choice = int(input("Select your drink (number): "))
            if drink_choice < 1 or drink_choice > len(drinks):
                print("Invalid choice. Please try again.")
                return self._get_drink_cost(drinks)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self._get_drink_cost(drinks)

        selected_drink = drinks[drink_choice - 1]
        selected_drink_cost = self.coffee_menu[selected_drink]['cost']

        print(f"The cost of {selected_drink.title()} is €{selected_drink_cost:.2f}.")
        return selected_drink, selected_drink_cost

    def _get_payment(self):
        """
        Prompts the user for the number of coins inserted for each currency,
        calculates total payment in euros, and returns that amount.
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
            return self._get_payment()

        total_inserted = (
                one_cent * self.euro_currency['one_cent'] +
                two_cents * self.euro_currency['two_cents'] +
                five_cents * self.euro_currency['five_cents'] +
                ten_cents * self.euro_currency['ten_cents'] +
                twenty_cents * self.euro_currency['twenty_cents'] +
                fifty_cents * self.euro_currency['fifty_cents'] +
                one_euro * self.euro_currency['one_euro'] +
                two_euros * self.euro_currency['two_euro']
        )
        return total_inserted

    def _get_change(self, selected_drink_cost, total_inserted):
        """
        Calculates and dispenses change if necessary.
        If there’s a shortfall, prompts for re-insertion of coins.
        """
        change = total_inserted - selected_drink_cost
        if change < 0:
            print(f"Insufficient funds. You are short: €{abs(change):.2f}. Please add more coins.")
            # If you want to force re-payment:
            additional_payment = self._get_payment()
            total_inserted += additional_payment
            return self._get_change(selected_drink_cost, total_inserted)
        else:
            print(f"Change: €{change:.2f}\nThank you! Enjoy your drink!\n")

    def _check_and_update_reservoir(self, drink):
        """
        Checks if there are enough ingredients to serve the drink.
        Deducts the ingredient amounts if sufficient.
        Returns True if served; False otherwise.
        """
        required_ingredients = self.coffee_menu[drink]["ingredients"]

        for ingredient, required_amount in required_ingredients.items():
            if ingredient not in self.reservoir:
                print(f"Error: {ingredient} is not available in the reservoir.")
                return False
            if self.reservoir[ingredient]["current_level"] < required_amount:
                print(f"Insufficient {ingredient} to serve {drink.title()}.")
                return False

        # Deduct from reservoir if all checks out
        for ingredient, required_amount in required_ingredients.items():
            self.reservoir[ingredient]["current_level"] -= required_amount

        print(f"{drink.title()} is served!")
        return True

    def _update_machine_state(self, drink):
        """
        Updates the machine's financial and operational state after successfully serving a drink.
        """
        cost = self.coffee_menu[drink]["cost"]
        self.machine_state["money"] += cost
        self.machine_state["drinks_served"][drink] += 1

    def _print_report(self):
        """
        Displays the current reservoir levels, total money, and drinks served count.
        """
        print("\n===== MACHINE REPORT =====\n")
        print("Reservoir Levels:")

        for ingredient, details in self.reservoir.items():
            current = details["current_level"]
            capacity = details["capacity"]
            unit = details["unit"]
            percentage = (current / capacity) * 100
            print(f"> {ingredient.title()}: {current}/{capacity} {unit} ({percentage:.1f}%)")

        print(f"\nTotal Money in Machine: €{self.machine_state['money']:.2f}")
        print("\nDrinks Served:")
        for drink, count in self.machine_state["drinks_served"].items():
            print(f"  {drink.title()}: {count}")
        print()


# -------------------------
#    USAGE EXAMPLE
# -------------------------
if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()






    



