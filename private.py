class Account:
    def __init__(self, name):
        self.__name = name
    def welcome(self):
        print("Welcome")
        self.__reset()

    def __reset(self):
        print(self.__name)

a1 = Account("Asru")
a1.welcome()