class pakoda:
    def isSpicy():
        print("pakoda is spicy")
    def isSweet():
        print("pakoda is not sweet")

class laddu:
    def isSpicy():
        print("laddu is not spicy")
    def isSweet():
        print("laddu is sweet")

def grtInfo(item):
    item.isSpicy()
    item.isSweet()

p=pakoda
l=laddu
grtInfo(p)
grtInfo(l)