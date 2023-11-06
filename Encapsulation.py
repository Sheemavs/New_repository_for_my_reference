class product:
    productPrice=0
    productName=""
    def __init__(self):
        self.productPrice=250
        self.productName="Apple"
    def ProductInfo(self):
        print(str(self.productName), "Product Price :", +self.productPrice)
    def getnewPrice(self,price):
        self.productPrice=price
        print("product crashed")
c=product()
c.ProductInfo()
i=[200, 150, 100]
for a in i:
    c.getnewPrice(a)
    c.ProductInfo()
