from abc import ABC,abstractmethod

class car(ABC):
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def printdetail(self):
        pass        
    def break_applied(self):
        print("car stopped")
    def accelaration(self):
        print("speed up....")

class hatchback(car):
    def printdetails(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("year:",self.year)
    def sunroof(self):
        print("not having this feature") 

car1=hatchback("maruti","alto","2020")           
car1.printdetails()
car1.accelaration()            
car1.sunroof()
car1.printdetail()
car1.break_applied()
