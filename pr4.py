class member:
    def __init__(self,roll_no=None,name=None):
        self.name=""
        self.roll_no=0
    # def accept(self):
    #     self.name=input("enter name:")
    #     self.roll_no=int(input("enter roll no:"))

    # def show(self):
    #     print(f"name:{self.name}   roll-no:{self.roll_no}")


# member1=member()   
# member2=member()   
# members=[member1,member2]

# for member in members:
#     member.accept()
# for member in members:
#     member.show()


class person(member):
    def __init__(self, roll_no=None, name=None,surname=None):
        super().__init__(roll_no, name)
        self.surname=""

    def take(self):
        self.name=input("enter name:")
        self.roll_no=int(input("enter roll no:"))
        self.surname=input("enter surname")   

    def display(self):
        print(f"name:{self.name}   roll-no:{self.roll_no}   suname:{self.surname}")
     


person1=person()   
person2=person()   
persons=[person1,person2]

for person in persons:
    person.take()
for person in persons:
    person.display()

