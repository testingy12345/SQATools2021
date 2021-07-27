"""
str1="Hello Good Morning, How are you ,we are learning Python"

expected_char = 'w'

for char in str1:
    if char == expected_char:
        print("We are breaking the loop")
        break
    else:
        print(char ,end= " ")
        continue
"""
"""
num = 1

while num <= 10:
    print(num)
    num=num+1
"""
################
"""
num = 1
table = 5
while num <= 10:
    print(num,"*" ,table ,":" ,num*table)
    num=num + 1
"""
###############################
#Write a python program to reverse the number
"""
num1=235
reverse= 0
while  num1 > 0:
   temp = num1%10
   reverse = reverse*10 + temp
   num1 = num1//10
   print("Reverse number is :" ,reverse)
"""
##########################
#Infinite loop
"""
num1 = 1
while True:
    print(num1)
"""
"""
num1 = 1
list1 =[]
while True:
    user_input = input("Please enter your number :")
    list1.append(user_input)
    if num1 == 5:
        break
        num1=num1+1
    print(list1)
"""
var ="Python"
var1=450
var2=2.25

str_format1="Hello this is var :"+var+",this is var1 :"+str(var1)+" and var2 :" +str(var2)
print(str_format1)

str_format2="Hello this is var :{},this is var1 :{} and var2 :{} ".format(var,var1,var2)
print(str_format2)

str_format3 =f"Hello this is var :{var},this is var1 :{var1} and var2 :{var2} "
print(str_format3)