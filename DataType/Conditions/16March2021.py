"""
1. Write a python script to parce the string and get all the employee id
from given string.

Input_str = "There are four employee with id emp_02 emp_405 emp_501 emp_605"
output = ['emp_02', 'emp_405', 'emp_501', 'emp_605']
"""
"""
Input_str = "There are four employee with id emp_02 emp_405 emp_501 emp_605"
output = []
str=Input_str.split()
print(str)
for value in Input_str:
    #print("Value :" , value)
    if value.isdigit():
        output= value=Input_str
        print("Output ",value)
        List=value
        print(List)
        List=type(value)
        #print(list)
        output=list
        #print(output)
"""
"""
Input_str = "There are four employee with id emp_02 emp_405 emp_501 emp_605"
output=[ ]
str=Input_str.split()
print(str)
id=['emp_02', 'emp_405', 'emp_501', 'emp_605']
if str==id:
    output= id.append()
    print(output)
"""
"""
3. Get all key and values from dictionary, covert all upper to lower.

dict1 = {'a': {'name': 'Rahul'},
'b': [5, 6, 7, 8, (4, 6)],
567 : (5, 7, 6, 'Python')
}
"""

"""
my_dict= {'a': {'name': 'Rahul'},
'b': [5, 6, 7, 8, (4, 6)],
567 : (5, 7, 6, 'Python')
}
new_dict=dict((k.upper(),v.upper()) for k ,v in my_dict.items())
print("The New Dictonary for upper case is : ",new_dict)
"""
"""
def upper_case(d):
    new_dict=dict((k.upper(),v) for k, v in d.items())
    return new_dict
my_dict= {'a': {'name': 'Rahul'},
'b': [5, 6, 7, 8, (4, 6)],
567 : (5, 7, 6, 'Python')
}
print(upper_case(my_dict))
"""
"""
def keys_upper(my_dict):
    res= dict()
    for key in my_dict.keys():
        if isinstance(my_dict[key],dict):
            res[key.upper()]=keys_upper(my_dict[key])
        else:
            res[key.upper()]=my_dict[key]
    return res
my_dict= {'a': {'name': 'Rahul'},
'b': [5, 6, 7, 8, (4, 6)],
'c' : (5, 7, 6, 'Python')
          }
print("The original dictonary :" + str(my_dict))
res=keys_upper(my_dict)
print("The modified dictonary : ",+ str(res))
"""
#############################
"""
Write a logic to get unique number number.
list = [5, 7, 8, 4, 3, 4, 5, 6, 7]
output = [5, 7, 8, 4, 6]
"""
"""
def unique(list):
    unique_list = [ ]
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)

list= [5, 7, 8, 4, 3, 4, 5, 6, 7]
unique(list)

print("The unique value from the list is" , unique(list))
unique(list)
"""
"""
1. Write a python script to parce the string and get all the employee id
from given string.

Input_str = "There are four employee with id emp_02 emp_405 emp_501 emp_605"
output = ['emp_02', 'emp_405', 'emp_501', 'emp_605']
"""
"""
Input_str = "There are four employee with id emp_02 emp_405 emp_501 emp_605"
output=[]
List_word=Input_str.split()
print(List_word)

for word in List_word:
    if "emp" == word.split("_")[0]:
        output.append(word)
    else:
        continue
print("output :" ,output)
"""
#2. Write a python string to re-write the string as expected output.

#input_str = "Its time to learn python programming"
#output = "iTS TiME To LeaRN PYTHoN PRoGRaMMiNG"
"""
input_str = "Its time to learn python programming"
output= ' '
vowel='aeiou'
for char in input_str:
    if char in vowel:
        output=output + char
    else:
        output=output+char.upper()
print(output)
"""
""""
3.Get all key and values from dictionary, covert all upper to lower.

dict1 = {'a': {'name': 'Rahul'},
'b': [5, 6, 7, 8, (4, 6)],
567 : (5, 7, 6, 'Python')
}
"""
"""
dict1 = {'a': {'name': 'Rahul'},
'b': [5, 6, 7, 8, (4, 6)],
567 : (5, 7, 6, 'Python')
}
str1 = 'a'
print(type(str1))

for k, v in dict1.items():
    print(k,":" , v)

    if str(type(k)) == "<class 'str'>":
         print(k.upper())
    else:
        continue

    if str(type(v)) == "<class 'dict'>":
        for k1 ,v1 in v.items():
            print(k1.upper(),v1.upper())
    elif str(type(v)) =="<class 'list'>":
         for data in v:
             print(data)
    elif str(type(v)) == "<class 'tuple'>":
        for data in v:
            print(data)
"""""
#########################################3
# 5. Write a python to get all phone number from the file.
# Condition: phone number should contain 10 digits.


#1 -> Get all lines from the file : file.readlines
#2 -> Go through each line using loop
#3 -> Get word list from each line using split method.
#4 -> Go through each word using loop
#5 -> Check word length should be 10 and word should contains on digit.
#6 -> if condition is true then append in phone_list
"""
phone_list = []
#1 -> Get all lines from the file : file.readlines

with open("phone_directory",'r') as file:
    all_lines=file.readlines()
 # 2 -> Go through each line using loop
    for line in all_lines:
# 3 -> Get word list from each line using split method.
      word_list=line.split()
#4 -> Go through each word using loop
      for word in word_list:
          if len(word)== 10 and word.isdigit():
              phone_list.append(word)
          else:
              continue
print("Phone List :", phone_list)
        
"""""
#6. Write to Python to get longest word in the string and change it from upper to lower.
"""
str1 = "Write to Python to get longest word in the GoodMorning and change it from upper to lower."
max_len =0
long_word = ''
#1 -> Get all word list from the string using split method.
#2 -> Go though each word and get the len of the word.
#3 -> compare word length with max_len, if word length if greater then set max_len=word_len
#     and set long_word = word
#4 -> Change upper to lower of the longest word.
#################################################
#1 -> Get all word list from the string using split method.
word_list=str1.split()
#2 -> Go though each word and get the len of the word.
for word in word_list:
    word_len=len(word)
    if word_len> max_len:
        max_len=word_len
        long_word=word
    else:
        continue
print("Max_Length :" ,max_len)
print("Long_Word :", long_word)
print(long_word.swapcase())
"""""
#7. Write a python program Get last two max numbers in the the list.
""""
list1 = [10, 50, 70 , 2, 45, 90, 22, 101]
#output = [101, 90]
Max_No=max(list1[0],list1[1])
secondMax_No=min(list1[0],list1[1])
output=[]
n=len(list1)
print(n)
for i in range (2,n):
    if list1[i]>Max_No:
        Maximum_No=Max_No
        Max_No=list1[i]
    elif list1[i]> secondMax_No and Max_No !=Max_No:
        Second_Max=list1

print("First Max No is ",Max_No)
print("Second Max No is ", secondMax_No)
"""""
##########################
# Write a python program to read file and get all odd and even line in seprate file
#along with replace "Python" with "SQATools"
#1.Go to lines of file .
#2. Go through each line using loop .
#3.Check index value of odd or even
#4.Check Python is available in the line or not
#5.If it is available then replace with SQATOOLS
#6.Add add and even lines in two seperate list.
#7. And those odd or even list in two seperate files.
"""
odd_lines=[]
even_lines=[]
#1.Go to lines of file .
with open("testfile.txt",'r') as file:
    alllines=file.readlines()
#2. Go through each line using loop .
    for i in range(len(alllines)):
        # 3.Check index value of odd or even

        if i%2==0:
            evenlines=alllines[i]
#4.Check Python is available in the line or not
            if "PYTHON" in evenlines:

                newline=evenlines.replace("PYTHON","SQATOOLS")
                even_lines.append(newline)
        else:
         even_lines.append(evenlines)

    else:
          oddlines = alllines[i]
if "PYTHON" in oddlines:
            newline = oddlines.replace("PYTHON", "SQATOOLS")
        odd_lines.append(newline)
     else:
        odd_lines.append(oddlines)
print("Even List :",even_lines)
print("Odd List :",odd_lines)
"""







