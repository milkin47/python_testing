class owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("This is parent class, ", self.name, self.age)

    def isEmp(self):
        print("True")

class emp(owner):
    def isEmp(self):
        print("False")

obj = owner("suresh", 20)
obj.display()
obj.isEmp()

obj1 = emp("David", 25)
obj1.display()
obj1.isEmp()