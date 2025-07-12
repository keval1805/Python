class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print(f"{self.year}{self.make}{self.model}")

car1=Car(" Toyota "," camry ",2020)
car2=Car(" honda "," accord ",2018)
car3=Car(" ford "," mustang ",2021)

cars=[car1,car2,car3]

for car in cars:
    car.display_info()