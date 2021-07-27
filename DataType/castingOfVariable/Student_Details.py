class student:
    def __init__(self,student_name,student_email):
        self.name=student_name
        self.email=student_email

    def show_student_name(self):
        print("Student name :",self.name)

    def show_student_email(self):
        print("Student email :",self.email)
