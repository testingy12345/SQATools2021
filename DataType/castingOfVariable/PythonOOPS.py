""""
class Car:
    def car_name(self):
        print("BMW")

    def car_prize(self):
            print("35 Lakh")

car_obj=Car()
car_obj.car_name()
car_obj.car_prize()

print("_"*50)
car_obj2 = Car()

car_obj2.car_name()
car_obj2.car_prize()
"""""
""""
class student:

    University_name="VIT"

    def __init__(self, name, age):
        self.st_name=name
        self.st_age=age

    def show_name(self):
        print(f"Student Name : {self.st_name}")

    def show_age(self):
        print(f"Student Age : {self.st_age}")

    def show_university(self):
        print(f"University Name :{self.University_name}")

st_obj=student('Vipin',30)
st_obj.show_name()
st_obj.show_age()
st_obj.show_university()
"""""


#Class & Object

"""
class A:
    def method1(self):
        print("We are in class A and Method1")

    def method2(self):
        print("We are in class B and Method2")
obj1 = A()
obj1.method1()
obj1.method2()
"""

"""
class B:
    def __init__(sqa, name, age):
        sqa.name=name
        sqa.age=age

    def show_name(sqa):
        print("Name :",sqa.name)

    def show_age(sqa):
        print("Age :",sqa.age)
obj2=B('Vipin',30)
obj2.show_name()
obj2.show_age()
"""
#Multilevel Inheritance
""""
class GrandFather:
    def __init__(self , degree):
        self.degree=degree

    def show_GrandFather_Degree(self):
        print("Grandfather degree : ",self.degree)

class father(GrandFather):
    def __init__(self , wealth,house,skill,degree):
        super().__init__(degree)
        self.wealth=wealth
        self.house=house
        self.skill=skill
        self.degree=degree

    def show_father_wealth(self):
        print("Father wealth is :",self.wealth)

    def show_father_house(self):
        print("Father house is :",self.house)

    def show_father_skill(self):
        print("Father skill is :",self.skill)

    def show_father_degree(self):
        print("Father degree is :",self.degree)

class child(father):
    def __init__(self, job, salary,skill,wealth,house,degree):
        super().__init__(wealth ,house,skill,degree)
        self.job=job
        self.salary = salary

    def show_child_job(self):
        print("child job :",self.job)

    def show_child_salary(self):
        print("Child salary :",self.salary)

    def show_child_skill(self):
        print("Child skill :",self.skill)

obj=child('IT',42000,'Cricket','50CR','Bagalow','MBBS')
obj.show_child_job()
obj.show_father_house()
obj.show_GrandFather_Degree()
obj.show_father_skill()
obj.show_child_skill()
"""""
################################3

#Multiple Inhertitance

"""
class father:
    def __init__(self, job,property):
        self.job=job
        self.property=property

    def shows_father_details(self):
        print("Father job :",self.job)
class mother:
    def __init__(self,Business):
        self.Business=Business

    def shows_mother_details(self):
        print("Mother Business :",self.Business)

class son(father,mother):
    def __init__(self , name ,job,property,Business):
        self.name=name
        super().__init__(job,property)
        self.mom=mother(Business)

    def shows_name(self):
        print("Name :",self.name)
obj=son('Harry','IPS','50CR','Handlooms')
obj.shows_father_details()
obj.shows_name()
obj.mom.shows_mother_details()
"""
#Single Inheritance
""""
class father:
    def __init__(self,wealth,house,skill):
        self.wealth=wealth
        self.house=house
        self.skill=skill

    def shows_father_wealth(self):
        print("Father Wealth is :", self.wealth)

    def shows_father_house(self):
        print("Father House :",self.house)

    def father_skill(self):
        print("Father skill is :",self.skill)

class child(father):
    def __init__(self, job, salary, wealth, house, skill):
        super().__init__(wealth ,house, skill)
        self.job=job
        self.salary=salary

    def show_child_job(self):
         print("Child job :",self.job)

    def show_child_salary(self):
        print("Child salary :",self.salary)

    def show_child_skill(self):
        print("Child skill :",self.skill)

obj=child('IT',42500,'Tennis' ,'10CR','Villas')
obj.show_child_job()
obj.shows_father_house()

obj.father_skill()
obj.show_child_skill()
"""""
###########################
