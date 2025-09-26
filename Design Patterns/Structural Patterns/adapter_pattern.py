#Paypal - third party class
class PayPal:
    def makePayment(self, amount):
        print(f"Payment made: {amount}")

#Target Interface - what client does
class PaymentMethod:
    def paymentMode(self, amount):
        pass

#Adapter Method
class PayPalAdapter(PaymentMethod):
    def __init__(self, paypal: PayPal):
        self.paypal = paypal
    
    def processMode(self, amount):
        self.paypal.makePayment(amount)

paypal_service = PayPal()
adapter = PayPalAdapter(paypal_service)
adapter.processMode(100)