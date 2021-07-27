"""
dict11={'a':456 , 'b':234 , 'c':121}
dict22={'x':'spider' ,'y':'jerms'}
dict22.update(dict11)
print("Dict22 :" ,dict22)
"""
"""
dictx = {'a': 456, 'b': 234, 'c': 121, 'd': 567}
print(dictx.items())
"""
"""
list1 = [5, 7, 8, 9]
list2 = ['A', 'B', 'C', 'D']
zipdata=zip(list1, list2)
for data in zipdata:
    print(zipdata)
"""
"""
dicty= {'a': 456, 'b': 234, 'c': 121, 'd': 567}
for k, v in dict.items():
    print(k, v)

for data in dicty:
    print(data)
"""
# Check any particular key is available in dictionary or not.
"""
dicty= {'a': 456, 'b': 234, 'c': 121, 'd': 567}
input_key ='f'
if input_key in dicty:
    print(True)
else:
    print(False)
"""
"""
str1 = 'Python'
output={ }
for char in str1:
    output[char] = char*3
print(output)
"""
"""
str1 = "Maintain two dict with vowel and consonant, char should be key and their could should value"
vowel_dict = { }
consonant_dict = { }
vowel='aeiou'
for char in str1:
    if char in vowel:
        v_count = str1.count(char)
        vowel_dict[char] = v_count
    else:
        c_count = str1.count(char)
        consonant_dict[char] = c_count
print("Vowel dict :", vowel_dict)
print("Consonant dict :", consonant_dict)
"""
