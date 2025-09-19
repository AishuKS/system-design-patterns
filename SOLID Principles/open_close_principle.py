from abc import ABC, abstractmethod

#abc - Abstract Base Class
# it is a python module that helps to create blueprint for class

#ABC - special base class from abc
# if a class inherits from ABC, then it becomes abstract class (cannot be
# directly used)

#@abstractmethod - it a way to tell, anyone who implements me should follow 
# the rule

 
class PaymentProcessor(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass

class PayPalPayment(PaymentProcessor):
    def processPayment(self, amount):
        print(f"Processing PayPal Amount: {amount}")
        
def main():
    processPayment = PayPalPayment()
    processPayment.processPayment(6000)
     
main()