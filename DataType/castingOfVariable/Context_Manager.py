"""
filename="context.txt"
with open(filename,'r') as file:
    data=file.read()
    print(data)

with open(filename, 'r') as file:
    print("begining position :" , file.tell())
    line=file.readline()
    print(line)
    print("position after reading 1 Line :" ,file.tell())
    file.seek(100)
    print("100 char movement from  begining :" , file.tell())
    Line2=file.readline()
    print("Line2 :" , Line2)
    print("Postion of 100 char movement read line :" , file.tell())
    file.seek(200,0)
    print("Position after 200 char movement :" , file.tell())
    Line3=file.readline()
    print("Line 3: ",Line3)
    print("Position 200 char move and readLine :" ,file.tell())
"""
    # Read all email from the file and add to the list.

    # 1 open file with context manager.
    # 2 read all lines using alllines method
    # 3 iterate through each line one by one using loop
    # 4 take word list from line using split method
    # 5 iterate through each word in wordlist using loop.
    # 6 check @ available in each word and consider it as email and add to email_list

    # 1 open file with context mana
filename="context.txt"

email_List=[]
with open(filename ,'r') as file:
     all_Lines=file.readlines()

     for Line in all_Lines:
         word_list=Line.split()
         print(word_list)

         for word in word_list:
             if '@' in word and ('.com' in word or 'co.in' in word):
                 email_List.append(word)
             else:
                 continue

print(email_List)
