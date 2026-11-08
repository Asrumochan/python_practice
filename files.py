# f = open("docs.txt","r")

# data = f.read()
# print(data)
# f.close()

# write files

# f = open("docs.txt","w")
# f.write("HI I AM ASRUMOCHAN ")
# f.close()

# f = open("sample.txt","a")
# f.write("PARIDA")
# f.close()


# create a new file 'practice.txt' using python Add data in it.

# with open("practice.txt","w+") as f:
#     f.write("Hi Everyone \nWe are learning File I/O \nusing Java \nI like programming in Java")

# WAF to replace all the java with python 

# with open("practice.txt",'r') as f:
#     data = f.read()

# new_data = data.replace("Java","Python")

# with open("practice.txt", 'w') as f:
#     f.write(new_data)

# Search if the word learning is exists or not

# with open("practice.txt","r") as f:
#     data = f.read()
#     found = data.find("learning")
#     if(found < 0):
#         print("Learning is not present in the file")
#     else:
#         print("Learning is present in the file")


#  WAF to find in which line of the file does the word 'learning' occur first. Print -1 if not found

# def check_line(word):
#     data = True
#     line = 1
#     with open('practice.txt','r') as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print("word found in line no.",line)
#                 return
#             line += 1
#     print(-1)
# check_line("pron")


#  From a file containing numbers separated by comma , print the count of the even numbers

# with open("nums.txt",'r') as f:
#     data = f.read().split(",")
#     print(len(data))
#     count = 0
#     for num in data:
#         if(int(num) % 2 == 0):
#             count += 1
#     print(count)
    
