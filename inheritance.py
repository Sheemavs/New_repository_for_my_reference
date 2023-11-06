class Car:
    def __init__(self, comp, mod):
        self.Company=comp
        self.Model=mod
    def getInfo(self):
        print(self.Company, self.Model)
ver1=Car("Lambo", "234")
ver2=Car("buka", "543")
ver1.getInfo()
ver2.getInfo()


class Car:
    def __init__(self, comp, mod):
        self.Company=comp
        self.Model=mod
ver1=Car("Lambo","234")
ver2=Car("buka", "543")

print(ver1.Company)