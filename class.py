# class Student:
#     college="ABC"
#     def __init__(self, name ,mark):
#         self.name = name
#         self.mark = mark
#         print("Parameterized constructor")
#     def welcome(self):
#         print("Welcome!", self.name, "Your mark is", self.mark)
#     def getMarks(self):
#         return self.mark
# #
# s1 = Student("Asru",90)
# # print(s1.name,s1.mark,s1.college)
# s1.welcome()
# print(s1.getMarks())


# Create student class that takes name and marks of 3 subjects as arguments in constructor and Then create one method to to print the average

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks= marks

    def getAverage(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return round(sum/3,2)

s1 = Student("Asru",[90,89,71])
print(s1.getAverage())