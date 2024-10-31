from abc import ABC,abstractmethod


#Step 1: Define the Strategy Interface 
class PayementMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass


#Step 2: Implement Concrete Strategies
class CreditCardPayment(PayementMethod):
    def pay(self, amount):
        return f"Paying {amount} using Credit Card"


class DebitCardPayment(PayementMethod):
    def pay(self, amount):
        return f"Paying {amount} using Debit Card"
    

class UPIPayment(PayementMethod):
    def pay(self, amount):
        return f"Paying {amount} using UPI"
    
class BitCoinPayment(PayementMethod):
    def pay(self, amount):
        return f"Paying {amount} using BitCoin"
    


#Step 3: Implement the Context
class ShoppingCart:
    def __init__(self,payment_nethod=PayementMethod):
        self.payment_method=payment_nethod

    def checkout(self,amount):
        return self.payment_method.pay(amount)
    


#Using Strategy in the Context
cart=ShoppingCart(CreditCardPayment())
print(cart.checkout(100))


cart=ShoppingCart(DebitCardPayment())
print(cart.checkout(100))


cart=ShoppingCart(UPIPayment())
print(cart.checkout(100))


