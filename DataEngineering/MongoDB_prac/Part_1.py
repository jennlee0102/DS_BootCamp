from random import randint

"""
Part 1
Class (Product Class & Tea Class)

[Product Class]
The drinks sold by CodeBeans are considered as (Product), and they all have the following fields (variables within the class) by default:
Name: name (string, default: none)
Price: price (integer, default: 30)
Size: size (integer, default: 20)
Warmth: warmness (float, default: 0.5)
Sweetness: sweetness (float, default: 0.5)
Identifier: identifier (integer, default: a random integer between 1000000 and 9999999)

Add two methods: sellability(self) & calory(self)

"""

class Product:
    def __init__(self, name=None, price=30, size=20, warmness=0.5, sweetness=0.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.size = size
        self.warmness = warmness
        self.sweetness = sweetness
        self.identifier = identifier

    def sellability(self):
        ratio = self.size / self.price
        if ratio < 0.5:
            return "Not so sellable..."
        elif ratio < 1.0:
            return "Kinda sellable."
        else:
            return "Very sellable!"

    def calory(self):
        cal = self.size * self.sweetness
        if cal < 10:
            return "...it's light"
        elif cal < 50:
            return "It's adequate."
        else:
            return "It's really heavy..!!"

        
"""
[Tea Class] Inheritance
- size default val = 10
- redefine calory method
    - always retrun "...it's a tea. Only a few calories"
- Add drink method
    - return the following message based on 'warmness'
        warmness < 0.5 : "it's too cold..."
        0.5 <= warmness0.5 <1.0 : "Oh, it's warm!"
        warmness >= 1.0 : "It's too hot!!"
"""

class Tea(Product):
    def __init__(self, size=10):
        super().__init__()
        self.size = size

    def calory(self):
        return "...it's a tea. Only a few calories"

    def drink(self):
        if self.warmness < 0.5:
            return "it's too cold..."
        elif self.warmness >= 0.5 and self.warmness < 1.0:
            return "Oh, it's warm!"
        else:
            return "It's too hot!!"