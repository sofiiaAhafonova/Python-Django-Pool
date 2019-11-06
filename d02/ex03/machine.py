import random
import beverages


class CoffeeMachine:
    """la machine à café"""

    def __init__(self):
        self.count = 0

    class EmptyCup(beverages.HotBeverage):
        def __init__(self, price=0.90, name="empty cup"):
            beverages.HotBeverage.__init__(self, price, name)

        def description(self):
            return "An empty cup?! Gimme my money back!"


    class BrokenMachineException(Exception):
        def __init__(self, msg="This coffee machine has to be repaired."):
            Exception.__init__(self, msg)

    def serve(self, beverage):
        print('use ', self.count)
        self.count += 1
        if self.count > 9:
            raise self.BrokenMachineException()
        return beverage() if random.randint(0, 1) == 0 else self.EmptyCup()

    def repair(self):
        self.count = 0
        print("\nMachine is repaired\n")


if __name__ == "__main__":
    for i in range(2):
        try:
            machine = CoffeeMachine()

            print(machine.serve(beverages.HotBeverage))
            print(machine.serve(beverages.Coffee))
            print(machine.serve(beverages.Coffee))
            print(machine.serve(beverages.Coffee))
            print(machine.serve(beverages.Tea))
            print(machine.serve(beverages.Tea))
            print(machine.serve(beverages.Cappuccino))
            print(machine.serve(beverages.Coffee))
            print(machine.serve(beverages.Tea))
            print(machine.serve(beverages.Tea))
            print(machine.serve(beverages.Cappuccino))
        except Exception as e:
            print(e)
            machine.repair()
