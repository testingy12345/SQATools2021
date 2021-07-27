# Program copy all files from one location to another
""""""
"""import os
import shutil
src_location="F:\\ToolsQA Python\\Browser"
tag_location="F:\\ToolsQA Python\\Practice"
#1. get list of files and folder from  source location, os.listdir(path)
data_list=os.listdir(src_location)
#2. iterate through each files and folder using loop
for item in data_list:
    print(item)
    # check item is file/folder
    # 3. create path for each file/folder using os.path.join(src_path, item)
    item_path=os.path.join(src_location,item)
    # 4. check item path is file or folder os.path.isdir(item_path) or os.path.isfile(item_path)
    if os.path.isfile(item_path):
        print(item)
        # 5. if we get tru to file path then copy file from source to destination : shutil.copy(src, tar)
        shutil.copy(item_path,os.path.join(tag_location))
    else:
        continue
"""
#####################################
# Create a small backup solution to copy all specific extension file in specific folder only.

"""import os
import shutil
src_location="F:\\ToolsQA Python\\Browser"
tag_location="F:\\ToolsQA Python\\Practice"
#1 -> Get all files and folder list : os.listdir(src_path)
Listdata=os.listdir(src_location)
#2 -> Iterate through each items in the list using loop.
for item in Listdata:
#3 -> create path of each item os.path.join(scr_path, item)
     item_path=os.path.join(src_location,item)
# 4 -> check if given path id file or folder
     if os.path.isfile(item_path):
# 5 -> if it is file then get a extension of file
        file_ext=item.split(".")[1]
# 6 -> create extension folder on target and copy the file.
        tar_dir=os.path.join(tag_location,file_ext)

        if os.path.isdir(tar_dir):
            shutil.copy(item_path, os.path.join(tar_dir ,item))

        else:
            os.mkdir(tar_dir)
            shutil.copy(item_path,os.path.join(tar_dir,item))
"""
#####################################
"""import  os
import  shutil
"""
#os module helps to interact with os function
#like , create folder, remove folder, get working directory
#create path, check file and folder.
"""
#Get the current working directory
cur_dir=os.getcwd()
print(cur_dir)
# Get list of all file and folder in given path
tar_path="F:\\ToolsQA Python\\Practice\\zip"
data_list=os.listdir(tar_path)
print(data_list)
print(len(data_list))
# Create folder in current dir
data_list1=os.mkdir("F:\\ToolsQA Python\\Nag")
print(data_list1)
#create folder in curent directory
data_list2=os.mkdir('Karnataka')
print(data_list2)
"""
"""import  os
import  shutil
str1='1'
print(os.getenv("C:\\Users\\veteran\\PycharmProjects\\pythonProject\\venv"))
os.system('control')
print(os.system('control'))
print(os.system('appwiz.cpl'))
print(os.system('notepad.exe'))
"""
##################################
#join two path
"""import  os
import  shutil
path1="F:\\ToolsQA Python"
path2="RMZ"
print(os.path.join(path1,path2))
filepath="F:\\ToolsQA Python\\New Text Document.txt"
print(os.path.isdir(filepath))
print(os.path.isfile(filepath))
# copy file from one location to another
shutil.copy(filepath,"E:\\Git.txt")
"""
#System Practice
import  sys

# Get file arguments
print(sys.argv)
#Get Factorial
"""fact=1
#for i in range(1, int(sys.argv[1])+1):
for i in range(1, int(sys.argv[1]) + 1):

    fact=fact*i

print("Factorial :",fact)
"""
"""userinput=input("Please Enter data")
userinput=sys.argv[1]
print(userinput)
print(userinput[::-1])
"""
print(sys.version_info)
print(sys.platform)
print(sys.api_version)

