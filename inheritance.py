
class Human:
    def __init__(self, name, add):
        self.name =  name
        self.add =  add
    
    def getData(self):
        print(self.name, self.add)

H = Human("Jay","UK")
H.getData()

class Student(Human):
    def __init__(self,name, add):
     super().__init__(name, add)

S = Student("Urmi","USA")

S.getData()