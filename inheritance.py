class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod 
    def start():
        print("Started !")

    @staticmethod    
    def stop():
        print("Stopped !")

class ToyotaCar( Car ):

    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

    def details(self):
        print("Car is ", self.name)


c1 = ToyotaCar("Fortuner","EV")
c1.details()
c1.start()
print(c1.type)

        