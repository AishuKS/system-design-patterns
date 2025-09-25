class Burger:
    def __init__(self, builder):
        self.cheese = builder.cheese
        self.onion = builder.onion
        self.tomato = builder.tomato
    
    def show_burger(self):
        print("Burger")
        print(f"Cheese: {"Yes" if self.cheese else "No"}")
        print(f"Onion: {"Yes" if self.onion else "No"}")
        print(f"Tomato: {"Yes" if self.tomato else "No"}")

class BurgerBuilder:
    def __init__(self):
        self.cheese = False
        self.onion = False
        self.tomato = False
    
    def add_cheese(self, c = True):
        self.cheese = c
        return self

    def add_onion(self, c = True):
        self.onion = c
        return self
    
    def add_tomato(self, c = True):
        self.tomato = c
        return self
    
    def build(self):
        return Burger(self)
    
burger1 = BurgerBuilder().add_cheese(True).add_onion(True).build()
burger1.show_burger()

burger2 = BurgerBuilder().add_cheese(True).build()
burger2.show_burger() 