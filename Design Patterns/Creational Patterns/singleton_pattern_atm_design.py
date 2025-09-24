# ------------ATM--------------
'''
Transactions
- cash withdraw
- cash deposit

Check balance

Change ATM Pin
'''

class ATMController:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Initializing ATM system")
            cls._instance = super().__new__(cls)
            cls._instance.balance = 10000
        return cls._instance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"Remaining Fund: {self.balance}")
        else:
            print("Insufficient Fund")
    
    def deposit(self, amount):
        self.balance+=amount
        print(f"New Balance: {self.balance}")

atm = ATMController()
atm.deposit(10000)
atm.withdraw(5000)