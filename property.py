class Student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str(round((self.phy + self.math + self.chem)/3 , 2)) + "%"

s1 = Student(98,89,93)
print(s1.percentage)
s1.phy = 87
print(s1.percentage)

