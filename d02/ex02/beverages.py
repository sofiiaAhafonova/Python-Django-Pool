class HotBeverage:
    def __init__(self, price=0.30, name="hot beverage"):
        self.price = price
        self.name = name

    def description(self):
        return "Just some hot water in a cup."
        
    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"


class Coffee(HotBeverage):

    def __init__(self):
        HotBeverage.__init__(self, price=0.40, name="coffee")

    def description(self):
        return  "A coffee, to stay awake."



class Tea(HotBeverage):

    def __init__(self):
        HotBeverage.__init__(self, name="tea")

    def description(self):
        return  "Just some hot water in a cup."
    
    


class Chocolate(HotBeverage):

    def __init__(self):
        HotBeverage.__init__(self, price=0.50, name="chocolate")

    def description(self):
        return  "Chocolate, sweet chocolate..."



class Cappuccino(HotBeverage):

    def __init__(self):
        HotBeverage.__init__(self, price=0.45, name="cappuccino")

    def description(self):
        return "Un po' di Italia nella sua tazza!"


if __name__ == "__main__":
	boisson_chaude = HotBeverage()
	print(boisson_chaude)
	cafe = Coffee()
	print(cafe)
	the = Tea()
	print(the)
	choco = Chocolate()
	print(choco)
	cappu = Cappuccino()
	print(cappu)
