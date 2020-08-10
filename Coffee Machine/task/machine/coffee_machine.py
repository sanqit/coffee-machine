import sys


class CoffeeMachine:
    def __init__(self):
        self.state = {
            "water": 400,
            "milk": 540,
            "beans": 120,
            "cups": 9,
            "money": 550
        }

        self.actions = {
            "buy": ("Buy some product", self.buy),
            "fill": ("Fill machine", self.fill),
            "take": ("Take off money", self.take),
            "remaining": ("remaining", self.remaining),
            "exit": ("Exit", sys.exit)
        }

        self.recipes = {
            "1": ("espresso", {"water": 250, "milk": 0, "beans": 16, "cost": 4}),
            "2": ("latte", {"water": 350, "milk": 75, "beans": 20, "cost": 7}),
            "3": ("cappuccino", {"water": 200, "milk": 100, "beans": 12, "cost": 6}),
            "back": ("to main menu",)
        }

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.state['water']} of water")
        print(f"{self.state['milk']} of milk")
        print(f"{self.state['beans']} of coffee beans")
        print(f"{self.state['cups']} of disposable cups")
        if self.state['money']:
            print(f"${self.state['money']} of money")
        else:
            print("0 of money")

    def print_actions(self):
        print(f"Write action ({', '.join(self.actions.keys())}):")

        current_action = input()
        print()
        return current_action

    def buy(self):
        drink_types = ", ".join(f"{key} - {self.recipes[key][0]}" for key in self.recipes.keys())
        drink_type = input(f"What do you want to buy? {drink_types}:\n")

        if drink_type == "back":
            return

        water = self.recipes[drink_type][1]["water"]
        milk = self.recipes[drink_type][1]["milk"]
        beans = self.recipes[drink_type][1]["beans"]
        cost = self.recipes[drink_type][1]["cost"]

        if self.state["water"] < water:
            print("Sorry, not enough water!")
            return

        if self.state["milk"] < milk:
            print("Sorry, not enough milk!")
            return

        self.state["water"] -= water
        self.state["milk"] -= milk
        self.state["beans"] -= beans
        self.state["cups"] -= 1
        self.state["money"] += cost
        print("I have enough resources, making you a coffee!")

    def fill(self):
        self.state["water"] += int(input("Write how many ml of water do you want to add:\n"))
        self.state["milk"] += int(input("Write how many ml of milk do you want to add:\n"))
        self.state["beans"] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.state["cups"] += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        money = self.state["money"]
        print(f"I gave you ${money}")
        self.state["money"] = 0

    def start(self):
        current_action = self.print_actions()
        while True:
            if current_action in self.actions:
                self.actions[current_action][1]()
            print()
            current_action = self.print_actions()


CoffeeMachine().start()
