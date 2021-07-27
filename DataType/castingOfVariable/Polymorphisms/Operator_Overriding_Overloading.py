class ABC:
    def __init__(self ,name,surname):
        self.name=name
        self.surname=surname

    def show_details(self):
        print("Name :",self.name)
        print("Surname :",self.surname)

    def show_msg(self):
        print("We are in class ABC")

class XYZ(ABC):

    def __init__(self ,age ,salary,name,surname):
        super().__init__(name,surname)
        self.age=age
        self.salary=salary

    def show_details(self):
        print("Age :",self.age)
        print("Salary :",self.salary)

    def addition(self):
        Str1='Hello'
        Str2='Afternoon'
        print(Str1+Str2)

    def addition(self):
        num1=500
        num2=589
        print(num1+num2)