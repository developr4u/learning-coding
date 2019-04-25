class Laptop:
    count = 0
    def __init__(self,name,model,price):
        Laptop.count += 1
        self.name = name
        self.model = model
        self.price = price

    def apply_disc(self,num):
        off = (num/100) * self.price
        return self.price - off 



l1 = Laptop('dell','core i3',52000)
l2 = Laptop('lenovo','core i4',25000)        
print(Laptop.count)


