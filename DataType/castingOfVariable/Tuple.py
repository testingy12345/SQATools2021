"""
tup=(4,8,7,5,2)
fact_list=[  ]
for num in tup:
    fact = 1
    for i in range(1, num+1):
        fact=fact*i
        fact_list.append((num,fact))
print(fact_list)
"""
dict1 = {'a' : 123, 'b': 456, 5: 'Hello'}

tup1=(7,5,6)
dict1[tup1]=[5,8,3,6]
#print(dict1)
allkeys =dict1.keys()
#print(allkeys)
allvalues = dict1.values()
#print(allvalues)
