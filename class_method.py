class Student:
    name = "Asru"

    @classmethod
    def changeName(cls, name):
        cls.name = name

s1 = Student()
s1.changeName("ABS")
print(s1.name)