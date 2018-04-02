class Vehicle:
    def __init__(self,now,tot,sc,max):
        self.now= now
        self.tot=tot
        self.sc=sc
        self.max=max

    def now(self):  #getter
        return self.now

    def now(self,nu): #setter
        self.now=nu


car = Vehicle(4,'ele',5,250)
print(car.now)
car.now=2
print(car.now) 
