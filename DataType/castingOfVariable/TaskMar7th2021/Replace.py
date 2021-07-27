# 1. replace your name with surname in given string. : using function

Str="Vipin"
print(Str)
def Surname(Str ,sur):
    sur="Tekade"
    Str=sur
    s1=Str.replace("Vipin","Tekade")
    print(s1)
    Surname(Str)
    print(sur)

"""Str="Vipin"
print(Str)
s1=Str.replace("Vipin","Tekade")
print(s1)
"""