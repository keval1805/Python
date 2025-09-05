class student:
    def __init__(self,sname=None,roll_no=None):
        self.sname=sname
        self.roll_no=roll_no

    def show(self):
        print(f"sname={self.sname} roll_no={self.roll_no}")

class book(student):        

    def __init__(self,bname,price,sname,roll_no):
        super.__init__(sname,roll_no)
        self.bname=bname
        self.price=price

    def display(self):
        print(f"bname={self.bname} price={self.price}")  

class branch(student):

    def __init__(self,branch_name,sname,roll_no):
        # super.__init__(sname,roll_no)

        self.branch_name=branch_name    

    def set(self):
        print(f"brach_name={self.branch_name}")




branch1=branch("cse","keval",145)
branch2=branch("cse-ai","Aayu",148)
branch3=branch("cse","soumya",143)
branch4=branch("cse","montu",144)

branch.set()





          