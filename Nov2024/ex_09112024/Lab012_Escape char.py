# Escape Character

sen1 = 'String'
sen2 = "String"
sen3 = ("String/n/n")

print(sen1)
print(sen2)
print(sen3)

""" r refers to raw data"""

print(r"C:\check's\n.txt")
print('C:check"s\n.txt')
#print('C:check's\n.txt') --- SyntaxError (unexpected character after line continuation character)


print("check's\t\ta")
print(r"check'u\t\ta")
#print(r"check"u\t\ta")  ---SyntaxError: unexpected character after line continuation character


