num1=50
#print(type(num1))
#int to string
var=str(num1)
#print(var)
#float to string
num2=56.2
#print(type(num2))
var1=str(num2)
#print(var1)
var2="x"
#print(var2+var1)
#string to int
str1='566'
#print(type(str1))
var3=int(str1)
#print(var3)
# list to tuple
List1=[5,6,3,7]
tup=tuple(List1)
#print(tup)
#################3
#String to list
Str="I am Working in Virtusa"
List2= list(Str)
#print(List2)
tup=tuple(List2)
#print(tup)
####
# dictionary to str
dict1 = {'a':'y','b':'z'}
#print(dict1)
#print(type(dict1))
#print(dict1['b'])
output2=str(dict1)
#print(output2)
#print(type(output2))
# we can not convert str to dict, it does not have key value pair.
print("#"*50)
#str2 = 'adfjadfjaskldfjasf'
#output3 = dict(str2)
#import jason
str1='{"a":900, "b":500, "c":2000}'
#output2=jason.dumps(str1)
#print(output2)
#print(type(output2))
# dict to tuple : it will return only keys in the tuple
dict1 = {'b':100,'z':456}
#print(type(dict1))
#print(dict1)
#################
list1 = [5,7,8,3]
list2 = [8,6,7,5]
var = zip(list1, list2)
#print(dict(var))
# str to set
set1 = {5,7,9,6}
var=str(set1)
####print(var ,type(var))
str2= "Good Night"
var2=set(str2)
#print(var2)
#print(type(var2))
## set to tuple and tuple to set
set1={4,8,5,3}
tup=tuple(set1)
#print(tup)
#==============
#tuple to set
tup=(4,5,7)
set=set(tup)
#print(set)
# Set to dictionary and dictionary to set
set={5,7,9}
dict1=dict(set)
#print(dict1)
#dic to set
dict2 = {'s': 456 ,'k' : 'vipin' ,'m' : 31}
str2 = str(dict2)

#print(list(str2))







