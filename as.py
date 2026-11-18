class Car:
    def __init__(self, type, **kwargs):
        super().__init__(**kwargs)
        self.type = type
        print("Car constructor")


class Vehicle:
    def __init__(self, brand, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        print("Vehicle constructor")


class ToyotaCar(Car, Vehicle):
    def __init__(self, name, type, brand):
        super().__init__(type=type, brand=brand)
        self.name = name
        print("Toyota constructor")


c1 = ToyotaCar("Fortuner", "EV", "Toyota")

print(c1.type)
print(c1.brand)