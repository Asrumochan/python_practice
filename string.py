str1 = 'Asrumochan'
str2 = "Hello, World!"
str3 = """This is a multi-line string.It can span multiple lines."""
str4 = '''This is another multi-line string.It can also span multiple lines.'''

character = str1[0]
print(character)  # Output: A

#Slicing
substring = str2[7:12]
print(substring)  # Output: World

substring2 = str2[:5]
print(substring2)  # Output: Hello

substring3 = str2[7:]
print(substring3)  # Output: World!

#negative indexing
last_character = str1[-1]
print(last_character)  # Output: n

substring4 = str1[-5:-1]
print(substring4)  # Output: ocha

