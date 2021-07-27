# 2. get count of all the character in string , print in dict. : using function
"""from DataType.castingOfVariable.Set import temp

i=0
temp[26]={0}
str=input("Enter your String")
for k in range(str):
    if (str[i])>='a' and str[i]<='z'):
        ++temp[str[i]-'a']
        print(temp)

    def printd(*temp):
        c='a'
        dict={}
        for i in range (*temp):
            dict[temp[i]]=c++
            dict{c++temp[i]}
            print(dict)
            """
"""test_str="Vipin"
all_char={}

for i in test_str:
    if i in all_char:
        all_char[i]+=1
    else:
        all_char[i]=1
#Printing the result
print("All chareter count is :\n" +str(all_char))
"""
def count_word(str):
    counts=dict()
    words=str.split()
    for word in words:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1

        return counts

print(count_word('I Love India'))


