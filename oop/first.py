class Laptop:
    def __init__(self,name,modle,price):
        self.name = name
        self.modle= modle
        self.price= price

l1= Laptop('hp', 'probook', 59000)
print(l1.name)