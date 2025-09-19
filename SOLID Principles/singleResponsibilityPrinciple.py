#without Single Responsibility Principle
class bakery:
    def bake_bread(self):
        print("Baking high quality bread")
    
    def manageInventory(self):
        print("Managing Inventory")

    def serveCustomer(self):
        print("Serving Customer")

#with Single Responsibility Principle
class BreadBaker:
    def bakeBreak(self):
        print("Baking bread")

class InventoryManager:
    def manageInvertory(self):
        print("Manage Inventory")

class SupplyOrder:
    def orderSupplies(self):
        print("Ordering Supplies")
        
def main():
    baker = BreadBaker()
    invertoryManager = InventoryManager()
    supplyOrder = SupplyOrder()
    
    baker.bakeBreak()
    invertoryManager.manageInvertory()
    supplyOrder.orderSupplies()

main()