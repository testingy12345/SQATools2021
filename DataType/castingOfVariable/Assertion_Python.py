num1=100
num2=500

"""
if num1==num2:
    print("Equal")
else:
    print("Not Equal")
"""
try:
    assert num1 == num2,"Checking number comparison"
    print("Operation Successful")
except Exception as e:

    print("Both number are not equal")
    #raise(e)
print("We are working on code module")