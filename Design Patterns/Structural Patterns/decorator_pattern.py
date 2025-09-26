from abc import ABC, abstractmethod
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 2
    
class MilkDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 0.5
    
coffee = SimpleCoffee()
print("Simple coffee:", coffee.cost())

coffee_with_milk = MilkDecorator(coffee)
print("Coffee with milk:", coffee_with_milk.cost())