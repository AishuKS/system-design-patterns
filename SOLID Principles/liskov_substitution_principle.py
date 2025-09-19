#violating LSP
class PaymentProcessor:
    def process(self, amount):
        print("Processing Payment")

class StrictPaymentProcessor:
    def process(self, amount):
        if amount<100:
            raise Exception("Amount is too small")
        print("Processing", amount)

strictpayment = StrictPaymentProcessor()
strictpayment.process(5)

#with LSP
class PaymentProcessor:
    def process(self, amount):
        if amount<100:
            raise Exception("Amount is too small")
        print("Processing Payment")

class StrictPaymentProcessor:
    def process(self, amount):
        print("Processing", amount)

strictpayment = StrictPaymentProcessor()
strictpayment.process(5)