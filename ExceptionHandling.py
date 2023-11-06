#1st
'''
item=0
if item!=2:
    raise Exception("item is not matching so giving exception")
'''
#2nd - Assertionerror
'''items=0
if items != 2:
    pass
assert(items==2) '''

'it will print Assertion error - if the value is zero then no error been dislayed'

#3rd - such that it will print except value

try:
    with open("nosuchfile.txt", 'r') as reader:
        reader.read()
except:
    print("given file is not present that is the failure")

print()
#4th - such that no error should display

try:
    with open("text.txt", 'r') as reader:
        reader.read()
except:
    print("given file is not present that is the failure")
finally:
    print("clean the txt file")

print()
#5th -  Exception Error and finally

try:
    with open("nosuchfile.txt", 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("clean the txt")
