"""
num= 21
if num%2 == 0:
    print("Even Number")
else:
    print("Odd Number")
    """
a=60
b=87
c=53
# # Find out bigger number
"""
if a > b and a >c :
     print("A is bigger Number :" , a)
if b > a and b > c:
    print("B is bigger Number : ",b)
if c > a and c >b :
    print("C is bigger Number : ", c)
"""
"""
if a > b or a >c :
     print("A is bigger Number :" , a)
if b > a or b > c:
    print("B is bigger Number : ",b)
if c > a or c >b :
    print("C is bigger Number : ", c)
"""
#% marks
"""
x=int(input("Enter your Marks :"))
if x >= 60:
    print("Congragtes you are pass with A+ Grade ")
if x >=50 and x<=60:
    print("Congragtes you are pass with A Grade ")
if x>=40 and x <=50:
    print("Congragtes you are pass with B Grade")
if x>=35 and x<=30:
    print("Congragtes you are pass with C Grade")
else:
    print("Sorry you are fail ")
"""
#5 Input from user divided by 5 or 7
#x= int(input("Plese enter the 5 numbers :"))
"""
x=50
x1=56
x2=63
x3= 70
x4 =75
x5= int(input("Plese enter the 5 numbers :"))
if x%5 == 0 and x1%5 == 0 and x2%5 == 0 and x3%5 == 0 and x4%5 ==0:
    print("Number is divided by 5")
if x%7 == 0 and x1%7 == 0 and x2%7 == 0 and x3%7 == 0 and x4%7 ==0:
    print("Number is divided by 7")
"""
#Item
"""
item1=45
item2=85
item3=190
item4=156
item5=145
Total=item1+item2+item3+item4+item5
print("The Total Amount is " ,Total)
#amt=int(input("Enter the amount :"))
def disc(args):
    pass


if Total>=500:
    disc=Total*0.2
    print("The Discount amount is ",disc)
    print("Discount :", disc)
    print("Net Pay :", Total - disc)
else:
    print("No Discount")

    print("Discount :",disc)
    print("Net Pay :",Total-disc)
"""
#Salary & Experience
"""
s=int(input("Enter user salary  :"))
e=float(input("Enter user Experience :"))
if e>=1:
    print("Give 10% increment in salary")
    print("The increment on user salary is :", s*0.1)
if e<=1:
    print("Give 5% increment in salary")
    print("The increment on user salary is :", s*0.05)
"""

#############################
"""
sal=float(input("Please enter salary of the employee :"))
exp=float(input("Please enter  experience of the employee :"))
if exp > 1:
    new_Salary=sal+sal*0.1
    print(new_Salary)
elif exp < 1:
    new_Salary=sal+sal*0.05
    print(new_Salary)
"""
######################33333
#Print Odd & even using for loop
"""
for j in range(50):
    if j%2 == 0:
        print("The Even no is :", j)
    else:
        print("The odd number is :", j)
"""
######################
"""
list1 = [ ]
for i in range(1, 6):
    num=int(input(f"Please enter the number :{i}"))
    list1.append(num)
print(list1)
"""
################3333
"""
List1 = [ ]
for i in range(1, 6):
    str1 = "Please enter num"+str(i)+ ":"
    num = int(input(str1))
    List1.append(num)
    print(List1)
"""

"""
for i in range(1, 6):

   num = int(input("Please enter the number "+str(i)+" :"))
if num%5 == 0 and num%7 ==0:
       print(num ,"It can divide :")
else:
       print(num ,"It cannot divide :")
"""
#Nested Loop Condition
for add in range(3):
    for parcel in range(5):
        print("address: " ,add ,"#parcel :" , parcel)

        print("#" *50)

#Get Combination of 2 number there sum should be 10
"""
List1=[5,8,6,7,4,2,1,3,9]
for var1 in List1:
    for var2 in List1:
        if var1 == var2:
            continue
        else:
            addition = var1 + var2
            print(("var1  :" ,var1,"|| var2 :",var2))
            if addition == 10:
                print(var1 , var2)
            else:
                continue

            print("#" * 50)
"""
#################################################
for i in range(1,20):
    if i == 4 or i ==7 or i ==15 :
        continue
    elif i == 8:
        break
    print(i , ": " , i*i)






