#  WAP to find the factorial of first n numbers

num = int(input("Enter the number:"))
fact = 1
for i in range(1,num+1):
    fact *= i
print("Factorial of ",num,"is",fact)