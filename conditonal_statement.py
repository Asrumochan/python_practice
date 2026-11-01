# # Vote
# age = int(input("Enter the age :"))

# if(age >=18):
#     print("You are eligible for vote!")
# else:
#     print("You are not eligible for vote!")

# #Grade
# mark = int(input("Enter the mark: "))
# if(mark >= 90):
#     print("grade: O")
# elif(mark < 90 and mark >= 80):
#     print("grade: A")
# elif(mark < 80 and mark >= 70):
#     print("grade: B")
# elif(mark < 70 and mark >= 60):
#     print("grade: B")
# elif(mark < 60 and mark >= 50):
#     print("grade: C")
# else:
#     print("You don't deserve the education!")

#Nesting

age = int(input("Enter the age :"))
if(age >= 18):
    if(age >= 80):
        print("Cannot Drive!")
    else:
        print("Can Drive !")
else:
    print("Cannot Drive !")

