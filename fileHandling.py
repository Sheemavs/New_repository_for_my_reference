#1st style of handling file
'''
file = open("text.txt")

print(file.readline())

file.close()
'''

#2nd style of handling file
'''
file = open("text.txt")

#using while loop readline been used
line=file.readline()
while line!='':
    print(line)
    line=file.readline()

#using for loop readlines been used
for line in file.readlines():
    print(line)

file.close()
'''

#3nd style of handling file

with open("text.txt",'r') as reader:
    content=reader.readlines()
    reversed(content)
    with open("text.txt",'w') as writer:
        for line in reversed(content):
            writer.write(line)