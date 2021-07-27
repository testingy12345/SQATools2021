"""
def read_file(filepath):
    fileobj=open(filepath,'r')
    data= fileobj.read()
    print(data)
    #name
    print("name :" , fileobj.name)
    print("mode : " , fileobj.mode)

filepath="C:\\Users\\veteran\\PycharmProjects\\pythonProject\\DataType\\castingOfVariable\\sample.txt"
read_file("sample.txt")
print("#"*50)
read_file(filepath)
"""
"""
def get_file_Line(filename='sample.txt'):
    fileobj=open(filename, 'r')
    line=fileobj.readline()
    print(line)

get_file_Line(filename='sample.txt')
"""
"""
def get_file_Line(filename='sample.txt'):
    fileobj=open(filename , 'r')
    line=fileobj.readlines()
    print(line)

get_file_Line(filename='sample.txt')
"""
"""
def get_file_line(filename='sample.txt'):
    fileobj=open(filename ,'r')
    all_Lines=fileobj.readlines()
    print(all_Lines)
    print(all_Lines[4])

get_file_line(filename='sample.txt')
"""
"""
file1=open('sample2.txt','r')
data=file1.read(10)
print(data)
line=file1.readline()
print(line)
"""
"""
def write_content_to_the_file(filename,str1):

    fileobj = open(filename , 'w')
    fileobj.write(str1)
    fileobj.close()

str1="Vipin Tekade .Working in Virtusa RMZ EcoWorld Bangalore"
write_content_to_the_file('demo.txt' , str1)
"""
"""
def append_data_to_file(filename,inputstr):
    fileobj=open(filename,'a')
    fileobj.write(inputstr)
    fileobj.close()

inputstr = 'Add data to the at the end, if file already exist add data at the end.'
inputstr2 = '\n Python Learning is Fun'

append_data_to_file('append_data_txt',inputstr2)
"""
str='Nagpur'
print(str[::-1])