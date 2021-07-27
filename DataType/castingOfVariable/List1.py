"""
Listx = [4,8,9,6,3]
listy = []
lenx=len(Listx)
print(lenx)
for var in range(lenx):
    temp=Listx.pop()
    listy.append(temp)

print("Listx :" , Listx)
print("Li,sty :", listy)
"""
#Adding Multiple element at a time
"""
lista=[8,7,2,3,6]
listb=[5,8,6]
print(lista.extend(listb))
print("Lista ",lista)
print("Listb ",listb)
"""
"""
lista =[5,6,2,7]
listb= [7,6,3,2]
listc = lista + listb
print("Listc ", listc)
print("Lista ", lista )
"""
#List Comphresion
# print square of all odd number
"""
List=[7,6,9,3,4,5]

for i in List:
    if i%2 !=0:
        print(i**2 , end=' ')
    else:
        continue
"""
"""
List=[7,6,9,3,4,5]
x=' '
print("/n")
[x for x in List]
result= [x**2 for x in List]
#print(result)
result2= [x**2 for x in List if x%2 != 0]
print(result2)

"""
"""
List1=[5,4,2,6]
List2=[5,7,6,3,8,9]
output=[ ]
for i in range(len(List2)):
    if len(List1) > i:
        output.append((List1[i],List2[i]))
    else:
        output.append(List2[i])
    print(i , output)
"""
#Program
""""
str1 = 'Python'
#output = [('P', 'pPpP'), ('y', 'yYyY'), ('t', 'tTtT'), ('h', 'hHhH'), ('o', 'oOoO'), ('n', 'nNnN')]
output=[]
for char in str1:
    temp =f"{char.lower()}{char.upper()}{char.lower()}{char.upper()}"
    combination=(char ,temp)
    output.append(combination)
print(output)
"""
