class teacher:
    def __init__(self,teacher_name,teacher_email):
        self.name=teacher_name
        self.email=teacher_email

    def show_teacher_name(self):
        print("Teacher name :",self.name)

    def show_teacher_email(self):
        print("Teacher email :",self.email)