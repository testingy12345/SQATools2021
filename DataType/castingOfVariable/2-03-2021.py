#1. Consider a list as input and create required dictionary
#list1 = [5, 6, 7, 8, 9]
#output = {5: 125, 6: 216, 7: 343, 8: 512, 9**3}
"""
list1 = [5, 6, 7, 8, 9]
output=''
for i in list1:
    print(i ," : " , i*i*i)
d1=zip(list1,output)
print(d1)
print (dict(d1))
"""
#2. get input string and print desired dictionary
#str1 = "We are learning Python"
#output = {'w' :'ew, 'a': ere, 'l':'gninrael', 'P': 'nohtyP'}
"""
str1 = "We are learning Python"
output={ }
str2=len(str1)
reverse=str1[str2::-1]
print(reverse)
combine=(str1, reverse)
output.append(combine)
print(combine)
"""
#1. Consider a list as input and create required dictionary
#list1 = [5, 6, 7, 8, 9]
#output = {5: 125, 6: 216, 7: 343, 8: 512, 9**3}
"""
List1=[5, 6, 7, 8, 9]
output={ }
for var in List1:
    print("var :" ,var**3)
    output[var] = var**3
print("Output :" ,output)
"""
#2. get input string and print desired dictionary
#str1 = "We are learning Python"
#output = {'w' :'ew, 'a': ere, 'l':'gninrael', 'P': 'nohtyP'}
#1. Get word list, using split method.
#2. Get each word from word list, using loop
#3. Get first char of each word, word[0]
#4. Get reverse of given word, word[::-1]
#5. store in dict first char as key and reverse of word as value
"""
str1 = "We are learning Python"
word_list=str1.split()
print(word_list)
result={ }
for word in word_list:
    print(word)
    first_word=word[0]
    print(first_word)
    reverse_word=word[::-1]
    print(reverse_word)
    result[first_word] = reverse_word
print("Result :" ,result)
"""
#3. read all dictionary values store in three seprate list for odd, even, str.
#dict1 = {'k1' : 23, 'k2': 14, 'k3': 25, 'k4': 56, 'k5': 'Hello', 'k6':'morning'}
"""
output:
list1 = [23, 25]
list2 = [14, 56]
list3 = ['Hello', 'morning']
"""
"""
#1. Get each key and value from the dict using: dict1.items()
#2. Check particular value is even then store in evenlist.  value%2==0
#3. check particular value is odd then store in odd list
#4. check particular value is str then store in string list
"""
dict1 = {'k1' : 23, 'k2': 14, 'k3': 25, 'k4': 56, 'k5': 'Hello', 'k6':'morning'}
odd_List=[]
even_List=[]
str_List=[]
for k ,v in dict1.items():
    print(k , " : " , v)
    if str(v).isdigit():
        if v%2 == 0:
            even_List.append(v)
        else:
            odd_List.append(v)
    else:
        str_List.append(v)

print("Odd_List :" ,odd_List)
print("Even_List : ",even_List)
print("String_List : " , str_List)
