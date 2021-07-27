from Python_OOPS.project.Student_Details import student
from Python_OOPS.project.Teacher_Details import teacher
from Python_OOPS.project.Account_Details import account

class school():
    def __init__(self,school_name,school_address,st_name,st_email,tech_name,tech_email,acc_name,acc_email):
        self.school_name=school_name
        self.school_address=school_address
        #self.st_email=st_email
        #self.tech_name=tech_name
        self.st_obj=student(st_name,st_email)
        self.tech_obj=teacher(tech_name,tech_email)
        self.acc_obj=account(acc_name,acc_email)

    def show_school_name(self):
        print("School Name :",self.school_name)

    def show_school_address(self):
        print("School Address :",self.school_address)
