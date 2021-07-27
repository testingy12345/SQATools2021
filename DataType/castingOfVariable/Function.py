"""
def show_msg():
    print("Hello, We started learning functional programming")
show_msg()
"""
# pass parameter to the function
"""
def show_msg2(msg):
    print("New Msg :" ,msg)

show_msg2("Good")
show_msg2("Morning")
"""
# functions parameter
"""
def function1(num1 ,num2):
    print(num1+num2)

x=40
y=50

function1(x,y)
function1(59,99)

function1('Hello','Morning')

def employee(name ,age,salary,email):
    print(f"Emp Name : {name}")
    print(f"Emp Age : {age}")
    print(f"Emp Salary : {salary}")
    print(f"Emp Email : {email}")

emp1= 'john'
age1= 45
salary1 = 78999
email1= 'john@test.com'

employee(emp1 ,age1 ,salary1,email1)

emp2= 'johnfds'
age2= 50
salary2 = 5555
email2= 'johndoe@test.com'

employee(emp2 ,age2 ,salary2,email2)
print("#"*100)
employee('ABC',45,45000,'a@gmail.com')
print("#"*100)
employee('BCa',55,65000,'b@gmail.com')
"""
"""
str1 ='Nagpur'
print(str1[-1:] )  #+ str1[1:-1] + str1[:1])
print(str1[1:-1])
print(str1[:1])
print(str1[-1:-1])
print(str1[-1:] + str1[1:-1] + str1[:1])
"""
"""
def function1(num1 ,num2 ,num3=80):
    print("Num1 :",num1)
    print("Num2 :",num2)
    print("Num3 :",num3)
    #print("Addition :",num1+num2+num3)


function1(50,20,30)
function1(num2=70,num3=20,num1=30)
function1(70,20,num3=30)
#function1(70,20,num1=30)
function1([4,7,8],{'a':125},'Hello')
"""
"""
def function2(*args,num1=54):
    print("Num1 :",num1)
    print(args)
    for var in args:
        print(var)

def function3(*sqa,num1=20):
    print("Num1 :",num1)
    print(sqa)
    for var in sqa:
        print(var)

function2(4, 6, 8, 'a', [4, 6, 7, 8], {'name':'rahul'}, (5, 7, 8), num1=50)
function3(5,6,7,8,3)
"""
# **kwargs : it helps to accept the arguments in the key value format.
"""
def function4(**kwargs):
    print(**kwargs)
    for k ,v in kwargs.items():
        print(k, ":" ,v)
        db_user='rahul123'
        db_pass='admin@123'

        if 'username' in kwargs and 'password' and kwargs:
            if db_user == kwargs['username'] and db_pass == kwargs['password']:
             f   print("Login Success")

            else:
                print('Invalid Credentials')
        else:
            print('Required inputs are not available')
"""
#function4(email='rahul@gamil.com', password='admin@1235')
# return : it enables function to return back the output

"""
def function5(num1,num2):
    multi=num1*num2
    print(multi)
    return multi

def addition(x,y):
    return x+y

var = function5(5,4)
print(var)
print(addition(var,60))

"""
"""
str='Mumbai'
print(str[:2])
print(str[2:])
"""
#Global Variable
""""
var1=60
def function1():
    print("We are in function1")
    var2=80
    print("Var1 global: ", var1)
    print("Var2 :" ,var2)

def function2():
    print("We are in function 2")
    var3= 100
    global var1
    var1= 200
    print("var3 :", var3)
    print("var1 global :"  ,var1)
    #print("var2" ,var2)
def function3():
    print("We are in function 3")
    var4= 90
    print("var4 :", var4)
    print("var1 global:" , var1)

print("#"*100)
function1()
print("#"*100)
function2()
print("#"*100)
function3()
"""""

#global
x=50

def outer_function():
    y=60

    def inner_function1():
        print("We are in inner function1")
        z=80
        print("x global :" , x)
        print("y non local: " ,y)
        print("z local :" , z)

    def inner_function2():
        print("We are in inner function 2")
        p=80
        nonlocal y
        y=500
        print("x global :", x)
        print("y non global:" , y)
        print("p local:",p)

    def inner_function3():
        print("we are in inner function3")
        q=100
        print("x global :",x)
        print("y non local :",y)
        print("q local :",q)

    inner_function1()
    print("#"*50)
    inner_function2()
    print("#"*50)
    inner_function3()
    print("#"*50)


outer_function()