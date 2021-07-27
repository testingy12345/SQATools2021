"""try:
    num=50
    output=num/12
    print(output)
    print("Division is successful :",output)
    print("Identation error is fixed")

except:
    print("Number cannot divide by zero")
"""
"""try:
    username=input("Please enter username :")
    password=input("Please enter password: ")

    db_user='vipin'
    db_password='P@ssword'
    if db_user == username and db_password == password:
        print("Login Successful")
    else:
        raise("Invalid Login")
except Exception as  e:
    print("Invalid credetial we cannot login")
    print(e)

finally:
    print("We are in home page")



###########################
"try:
    name="Vipin"
    num=586
    print(name+num)
except:
    print("Cannot add number and string")
else:
    print("Concatnation Succcessful")
    """
#Lamda function

"""result=lambda x, y: x+y
print(result(60,555))
"""
"""result1=lambda x ,y:(x+y)*2
print(result1(55,789))
"""
"""result2=lambda x ,y : x if x%2 ==0 else y
print(result2(59 , 36))
"""
#Map

"""def square(n):
    return n**2
list1 =[5,7,3,8,9]
output=list(map(square ,list1))
print(output)
output1=list(map(lambda x:x//2 ,list1))
print(output1)
"""
def factorial(num1):
    fact=1
    for i in range(1 ,num1+1):
        fact=fact+i/0

        return fact

try:
    print(factorial(10))
except Exception as e:
    raise e