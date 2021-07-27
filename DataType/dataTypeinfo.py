List=[4,8,9,'a','hello',[7,8,9]]
#print(List)
output=List[-3]
#print(output)
out2=List[2]
#print("Output :" ,out2)
######
#print(List[2:4])
#print(List[2:-3])
#print(dir(List))
#####
#Tuple
tup=(8,7.3,'a',[4,8,6,5],'YMZ')
#print(tup[3][3])
#print(dir(tup))
###################
dict1={'name':'Vipin',(5,8,3):854,'Afternoon':'y','z':[5,7,9]}
#print(dict1)
#print(dict1['Afternoon'])
output=dict1['z']
#print(output)
#Adding another value
dict1['surname']= 'Tekade'
#print(dict1)
#For All Keys
keys=dict1.keys()
#print(" keys :" ,keys)
#For All Values
values=dict1.keys()
#print("values ",values)
#print(dir(dict))
#['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
## we can not define list as key
# for ex #dict1[[4, 6, 7]] = 'Python'
#Set
set1={4,5,5,6,9,'h',4}
#print(set1)
set1.add(1000)
#print(set1)
## We can not add list inside of set
#set1.add([4, 6, 8])
#print(set1)
#==================
# We can not add dict in the set

#set1.add({'a': 234, 'b':456})
#print(set1)
###############
# Methods available in the set
#print(dir(set1))
#['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
##################
List= [5,8,9,66,56,66,5]
#print(set(List))
#Boolean
a=10
b=52
#print(a>b)
#print(b>a)
#####################
str1="live long life"
#print(str1[2::-1])
#print(str1[4::-1])



