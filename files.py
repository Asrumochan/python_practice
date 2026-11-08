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

with open("practice.txt","r") as f:
    data = f.read()
    found = data.find("learning")
    if(found < 0):
        print("Learning is not present in the file")
    else:
        print("Learning is present in the file")