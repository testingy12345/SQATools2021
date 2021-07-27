from Python_OOPS.project.School_Manegment import school
school_name="IRA INTERNATIONAL"
school_address="Chennai"
st_email="a@gmail.com"
st_name="XYZ"
tech_name="Mary"
tech_email="m@gmail.com"
acc_name="Ronit Roy"
acc_email='r@gmail.com'

sch_obj=school(school_name,school_address,st_name,st_email,tech_name,tech_email,acc_name,acc_email)

sch_obj.st_obj.show_student_name()
sch_obj.st_obj.show_student_email()

sch_obj.tech_obj.show_teacher_name()
sch_obj.tech_obj.show_teacher_email()

sch_obj.acc_obj.show_account_name()
sch_obj.acc_obj.show_account_email()