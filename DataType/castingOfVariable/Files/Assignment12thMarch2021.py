#Assignment
#1 Create 5 recursive folder , it means one folder inside another folder, and create one text file in each folder.
"""import os
import  shutil
tar_dir="F:\\ToolsQA Python\\Nag"
folder_path=tar_dir
Input_Str="Create 5 recursive folder , it means one folder inside another folder, and create one text file in each folder."
#1 : Initiate one loop from 1 to 6. using range.
for i in range(1,6):
    print("i :",i)
    folder_name=f"folder_{i}"
    # 2 : Create a folder on target directory and update the path with folder that we have created.
    folder_path="F:\\ToolsQA Python\\Nag","F:\\ToolsQA Python\\Nag\\folder_1"
    folder_path=os.path.join(folder_path,folder_name)
    #folder_path="F:\\ToolsQA Python\\Nag\\folder_1","F:\\ToolsQA Python\\Nag\\folder_1\\folder_2"
    #folder_path=os.path.join(folder_path,folder_name)
    #folder_path="F:\\ToolsQA Python\\Nag\\folder_2","F:\\ToolsQA Python\\Nag\\folder_1\\folder_3"
   # folder_path=os.path.join(folder_path,folder_name)
    #folder_path="F:\\ToolsQA Python\\Nag\\folder_3","F:\\ToolsQA Python\\Nag\\folder_1\\folder_4"
    #folder_path=os.path.join(folder_path,folder_name)
    #folder_path="F:\\ToolsQA Python\\Nag\\folder_4","F:\\ToolsQA Python\\Nag\\folder_1\\folder_5"
    #folder_path=os.path.join(folder_path,folder_name)
    print("folder_path :",folder_path)
    os.mkdir(folder_name)
    # 3 : create file in each folder path.
    file_name=f"filename_{i}.txt"
    folder_path=os.path.join(folder_path,folder_name)
    print("File_Path :",folder_path)
    with open(folder_path,'w') as file:
        file.write(Input_Str)

        print("#"*100)
sum=0
for i in range(1,10):
    sum=sum+i
"""
#####################################################
#2) Copy files from one location to another location with different name.
"""import os
import shutil
src_location="F:\\ToolsQA Python\\Nag"
tar_location="F:\\ToolsQA Python\\Browser"
new_name = ['shiv', 'vipin', 'zafar', 'aditi', 'pooja', 'shivleela']
#a. get all files from scr location using os.listdir()
List_data=os.listdir(src_location)
#b. iterate through each file in list data. using loop
temp=0
for file in List_data:
    # c. create a src_file and tar_file path with different.
     src_file_path=os.path.join(src_location,file)
     tag_file_location=os.path.join(tar_location,f"{new_name[temp]}.txt")
    # d.  copy file from one location to another location
     shutil.copy(src_file_path,  tag_file_location)
temp=temp+1
"""
#3 Copy only specific files from one location to another another location
#consider these three files should be copied ['file1.txt', ''file2.txt', 'file2.txt'] apart from 100 files in the folder.
"""import os
import shutil
src_location="F:\\ToolsQA Python\\Nag"
tar_location="F:\\ToolsQA Python\\Browser"
required_names=['file1.txt', 'file2.txt', 'file2.txt']
#a). Get allfiles and folder list using os.listdir()
listdata=os.listdir(src_location)
#b). Iterate through each file using loop.
for file in listdata:
    #c). verify each file name and compare with existing file.
    if file in required_names:
        src_filepath=os.path.join(src_location,file)
        tar_filepath=os.path.join(tar_location, file)
        # d). If file name match then copy it.
        shutil.copy(src_filepath,tar_filepath)
    else:
      continue
"""
#4 Create 1000 files in the folder with different extension 100:txt 100:png, 100 : jpg..... like this
import os
import shutil
src_location="F:\\ToolsQA Python\\Nag"
tar_location="Create 1000 files in the folder with different extension 100:txt 100:png, 100 : jpg..... like this"
#a) create list of extesion.
ext_list = ['jpg', 'jpeg', 'xls', 'bin', 'mp4', 'mp3', 'kvm', 'json', 'txt', 'png']
#b) initiate a loop from 1 to 1000.
temp=0
ext_range=0
for i in range(1, 1000):
    if ext_range < 100:
        # c) Start creating 100 file with each extension in the target location
      file_path=os.path.join(tar_location,f"filename_{ext_range}.{ext_list[temp]}")
      with open(file_path,'w') as file:
        file.write(tar_location)
    print("ext_range , temp :" ,ext_range ,temp, ext_list[temp] , i)
    ext_range = ext_range +1

else:
    ext_range=0
    temp=temp+1

print("#"*250)
###############################
""""""
#Small Assignment for Function

# Assignment :
# 1. replace your name with surname in given string. : using function
# 2. get count of all the character in string , print in dict. : using function
# 3. get 'python' as string and return dict like below output.
#dict = {'p' : '###p###', 'y': '__y__', 't': '++t++', 'h': '??h??', 'o':'==0==', 'n':'**n**'}
#4. Create a simple calculator which has option add, multiply, substract and divide

#each action should be calculated via function and ask user which action he wants to perform ,

#1. Addition
#2. Mulitplication
#3 Substraction
#4 Divide

#as per user choice calculate the stuff
