from os import listxattr

list1=[7,8,9,5,'a','Hello']
#print(list1[0])
#print(list1[-6])
list1.append(40)
#print(list1)
list1.insert(4,50)
#print(list1)
output=list1.remove(7)
#print(list1)
#print("output" ,output)
print("#"*50)
list2=[5,8,9,6,3]
output=list2.pop()
#print("Output :",output)
#print(list2)
#pop with specific index
output=list2.pop(3)
#print(output)
#print(list2)
#######################
"""
Listx = [4,8,9,6,3]
listy = []
lenx=len(Listx)
print(lenx)
for var in range(lenx):
    temp=Listx.pop()
    listy.append(temp)

print("Listx :" , Listx)
print("Listy :", listy)
"""
"""
listx = [5, 7, 8, 9, 34]
listy = []
lenx = len(listx)
for var in range(lenx):
    temp = listx.pop()
    listy.append(temp)

print("Listx", listx)
print("Listy", listy)
"""
"""
Lista =[5,8,6,7]
listb = [4,7,6]
print(Lista.extend(listb))
"""
lists = [6, 5, 3, 2, 7, 5, 5]

#count
print("count 5:", lists.count(5))