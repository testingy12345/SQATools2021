#Lower to upper

stra = " Hello ,Good Morning"
"""
print(stra.swapcase())
new_str = " "
for char in stra:
    print(char)
    if char.isupper():
        new_str = new_str + char.upper()
    elif char.islower():
        new_str = new_str +char.lower()
    else:
        new_str = new_str +char
print(new_str)
"""
#print(stra.upper())
#print(stra.lower())
"""
strb = " xyz "
print(strb)
print(strb.strip())
"""
"""
strc=" GJHHJ "
print(list(strc))
"""
"""
strc=" GJHHJ "
output= strc.split(" ")
print(output)
print(type(output))
print(output[0] , type(output[0]))
"""
str11 ="Split the string on the basis of delimeters"
"""
word_list=str11.split(" ")
print(word_list)

for word in word_list:
    print(word ," : " ,word[::-1])
"""
#print(str11.istitle())
#print(str11.title())
"""
str5="Python 29"
for char in str5:
    print(char ," : " , char.isdigit())
"""
"""
str54="Check if any digit is available or not"
#print(str54.count("i"))

temp_str=" "
for char in str54:
    if char in temp_str:
        continue
    else:
        print("temp_str : " , temp_str)
        print(char ," : " ,str54.count(char))
        temp_str = temp_str + char
"""
#Get the max length word of string
"""
str55 = "Check if there is any digit is available or not  gsdfgjdfsgjsdfklg"
word_list=str55.split(" ")
print(word_list)
max_len= 0
exp_word= " "
for word in word_list:
    word_length=len(word)
    print(word ," : " , word_length)
    if word_length > max_len:
        max_len=word_length
        exp_word=word
        print("Max Length : ",max_len)
        print("Expected Length :" , exp_word)
    else:
        continue
        print("####################")

print("Max Length : ", max_len)
print("Expected Length :", exp_word)
"""
#########################33
# Get min length word from the string.
"""
str55 = "Check if there is any digit is available or not  gsdfgjdfsgjsdfklg"
word_list=str55.split(" ")
print(word_list)
min_len=len(word_list[0 ])
exp_word=''
for word in word_list:
    word_length=len(word)
    print(word," : " ,word_list)
    if word_length <= min_len:
        min_len=word_length
        exp_word =word
        print("Min_Length :" ,min_len)
        print("exp_word : " ,exp_word)
    else:
        continue
        print("#####################")
print("Min_Length :", min_len)
print("exp_word : ", exp_word)
"""
####################################################
#Most simultanneously repeated charecter of the string .
"""
str77 = "sssdadfasdfa ggggg ffffffffffff"
print("#"*50)
char_count = 1
exp_char = ' '
max_char_len=1
for i in range(len(str77)-1):=
    print("char_count :" ,char_count)
    print("char :" ,str77[i])
    print("max_char_len : ", exp_char)
    if str77[i] == str77[i+1]:
        char_count+=1
        if char_count > max_char_len:
            max_char_len=char_count
            exp_char= str77[i]
        else:
            char_count = 1
            print("#"*50)

print(char_count)
print(max_char_len," : " ,exp_char)
"""
##################################
"""
str1="Pyhon"
#print(str1[::-1])
output=reversed(str1)
print(output)
#print(str1.reversed())

str1= ' '
for data in output:
    print(data)
    str1= str1 + data
    print(str1)
"""

#################################
"""
str1="Pyhon"
new_str=" "
for i in range(-1,-len(str1)-1, -1):
    print(i)
    new_str = new_str + str1[i]
print(new_str)
print("#"*100)
print(len(str1))
"""
###########################
""""
str1="Pyhon"
for i in range(-1,-len(str1)-1,-1):
    print(i,str1[i])
"""
############################
"""
str1="Pyhon"
print("length :",len(str1))
"""
"""
str1="Pyhon"
"""
"""
for i in range(0,5,1):
    print(i)
"""
""""
for j in range(-1,-len(str1)-1,-1):
    print(j ,str1[j])
"""
#########################
#find char and substring in string
"""
str22 = "find char and substring in the string."
print(str22.find('in'))

output = True if 'a' in str22 else False
print(output)
"""
########################
# 1. create a new string with all odd places character.
"""
str1 = "find char and substring in the string."
count=len(str1)
for char in str1:
    if count % 2!=0:
        print(char)
        count+=1
    else:
        count+=1
"""
"""
str1 = "find char and substring in the string."
odd_string=''
even_string=''

for index in range(len(str1)):
    if index %2 !=0:
        odd_string=odd_string+str1[index]
        print(odd_string)
    else:
        even_string=even_string+(str1[index])
"""

#2. replace 'and' with 'or' and change the case of each character.
"""
str1 = "find char and substring in the string."
output=str1.replace("and","or")
print(output)
print(output.upper())
print(output.lower())
"""
#########################################
#3. check specific substring is available in the string and get count of it.
"""
str1 = "find char and substring in the string."
str2= "substring"
count = str1.count(str2)
print("The count is :" ,count)
"""
#################################################3
#9). Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

line1 = 'djsdfksjafa J sdfasdf HJ dfdsH Good Mornirg'
line2 = 'Hello How are you'
line3 = 'We are learning Python Programsing'
line4 = 'Skilled persons are Required in The industry'
line2=[line1,line2 , '' ,line3,line4]
for line in line2:
    if line == '':
        continue
    else:
        print(line.lower())
