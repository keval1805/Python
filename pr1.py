class Bank:
    def __init__(self,add=None,bankname=None):
        self.add=add
        self.bankname=bankname
        
    def display(self):
        print(f"{self.add}{self.bankname}")

# bank1=Bank(" vadodara "," sbi ")
# bank2=Bank(" navsari "," hdfc ")
# bank3=Bank(" surat "," icic ")
# banks=[bank1,bank2,bank3]
# for Bank in banks:
#     Bank.display()

class customer(Bank):
    def __init__(self,name=None,add=None,bankname=None):
        self.name=name
        
        
    def show(self):
        print(f"{self.name}")

customer1=customer(" keval ")
customer2=customer(" param ")
customer3=customer(" montu ")
customers=[customer1,customer2,customer3]
for customer in customers:
    customer.show()


class account:
    def __init__(self,accno):
        self.accno=accno
        
        
    def get(self):
        print(f"{self.accno}")

account1=account(" 001 ")
account2=account(" 002 ")
account3=account(" 003 ")
accounts=[account1,account2,account3]
for account in accounts:
    account.get()
