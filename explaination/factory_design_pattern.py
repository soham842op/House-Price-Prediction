from abc import ABC,abstractmethod

#Step 1: Define Product Interface
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass


#Step 2 : Implement Concrete Products

class Espresso(Coffee):
    def prepare(self):
        return "Preparing a Rich and Strong Espresso"
    
class Latte(Coffee):
    def prepare(self):
        return "Preparing Smooth and Creamy Latte"


class Cappuccino(Coffee):
    def prepare(self):
        return "Preparing a Frothy Cappuccino"
    

#Step 3 : Implement the Factory (CoffeeMachine)

class CoffeeMachine:
    def make_coffee(self,coffee_type):
        if coffee_type=="Espresso":
            return Espresso().prepare()
        elif coffee_type=='Latte':
            return Latte().prepare()
        elif coffee_type=='Cappuccino':
            return Cappuccino().prepare()
        else:
            return "Unknown Coffee Type"
        

#Step 4: Use the factory to create Products

machine=CoffeeMachine()

coffee=machine.make_coffee("Espresso")
print(coffee)


coffee=machine.make_coffee("Latte")
print(coffee)

coffee=machine.make_coffee("Cappuccino")
print(coffee)
