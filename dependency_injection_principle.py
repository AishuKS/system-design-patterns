#without DIP
class PayPal:
    def paymentProcessor(self, amount):
        print(f"Process payment {amount}")


payment = PayPal()
payment.paymentProcessor(500)

#with DIP
from abc import ABC, abstractmethod

# Abstraction
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount): pass

# Implementations
class PayPal(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} via PayPal")

class CreditCard(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} via Credit Card")

# High-level module depends only on abstraction
class Checkout:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def complete_order(self, amount):
        self.processor.pay(amount)
        print("Order completed")
