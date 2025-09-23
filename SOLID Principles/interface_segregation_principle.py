from abc import ABC
class Vegeterian(ABC):
    def getVegeterianMenu(self):
        print("Vegeterian Menu")

class NonVegeterian(ABC):
    def getNonVegeterianMenu(self):
        print("Non Vegeterian Menu")
    
class Drinks(ABC):
    def getDrinks(self):
        print("Drinks Menu")

vegeterian = Vegeterian()
nonVegeterian = NonVegeterian()
drinks = Drinks()

vegeterian.getVegeterianMenu()
nonVegeterian.getNonVegeterianMenu()
drinks.getDrinks()