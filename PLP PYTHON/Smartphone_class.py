# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

    def details(self):
        return f"{self.brand} {self.model}, Price: ${self.price}"

# Derived class: Smartwatch
class Smartwatch(Smartphone):  # Inherits from Smartphone
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life
    
    # Polymorphism: Overriding the details method
    def details(self):
        return f"{self.brand} {self.model} (Smartwatch), Price: ${self.price}, Battery Life: {self.battery_life} hours"

# Creating objects
phone = Smartphone("Apple", "iPhone 14", 999)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 399, 48)

# Using the objects
print(phone.details())
phone.make_call("123-456-7890")
phone.send_message("123-456-7890", "Hello!")

print(watch.details())
watch.make_call("987-654-3210")  # Inherited method
