from abc import ABC, abstractmethod

# Component
class Employee(ABC):
    @abstractmethod
    def show_details(self):
        pass

# Leaf
class Developer(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def show_details(self):
        print(f"{self.role}: {self.name}")

# Leaf
class Designer(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def show_details(self):
        print(f"{self.role}: {self.name}")

# Composite
class Manager(Employee):
    def __init__(self, name):
        self.name = name
        self.subordinates = []
    
    def add(self, employee: Employee):
        self.subordinates.append(employee)
    
    def remove(self, employee: Employee):
        self.subordinates.remove(employee)
    
    def show_details(self):
        print(f"Manager: {self.name}")
        for emp in self.subordinates:
            emp.show_details()

# Client
dev1 = Developer("Alice", "Frontend Dev")
dev2 = Developer("Bob", "Backend Dev")
designer = Designer("Charlie", "UI Designer")

manager = Manager("Eve")
manager.add(dev1)
manager.add(dev2)
manager.add(designer)

manager.show_details()
