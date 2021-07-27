set1 = {5, 7, 8, 2, 5, 6, 'a', 'Hello'}
#print(type(set1))
output=set1.pop()
#print("output :",output)
#Update
seta = {'a','b','c'}
setb = { 3,6,8,'a'}
seta.update(setb)
#print("Set a :" ,seta)
# union : get all unique elements from both the sets
r_set=seta.union(setb)
#print(r_set)
#print("Set a",seta)
#print("Set b",setb)
# difference : get difference values from one set to another.
print("#"*20)
setp = {'d', 'c', 'a', 'b', 6}
setq = {8, 3, 'a', 6}
#print(setp.difference(setq))
# sysmmetric difference : get all unique value from both the sets, and avoid duplicate values.
#print(setp.symmetric_difference(setq))
# shallow copy
setp = {'d', 'c', 'a', 'b', 6}
setr=setp
setr.add(77)
#print("set r : ",setr)
#print("Set q : " , setq)

setx = {'d', 'c', 'a', 'b', 6}
sety=setx.copy()
sety.add(66)
#print("setx :",setx)
#print("sety :",sety)

#Check subset
setz = {'a', 'b', 66, 6, 'd', 'c'}
temp = {'a', 'b', 44}
#print(temp.issubset(setz))

# Add different data in set
setp =['g','h',6,7]
#print(setp)
#setp.add((6,7,8))
#print("Set p :", setp)

# add list to set : adding list to set is not allowed

list1 = [5, 2, 45, 34]
#setp.add(list1)

# add dict to set : adding dict to set is not allowed.
#setp.add({'name':'John','age':67})
#print(setp)
# Get all unique value from list
list1 = [5, 7, 8, 3, 9, 2, 5, 3, 2, 3]
#print(set(list1))
set2 = set()
for i in list1:
    set2.add(i)
#print(list(set2))
