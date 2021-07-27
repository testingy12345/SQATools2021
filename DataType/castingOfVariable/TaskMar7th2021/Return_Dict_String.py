# 3. get 'python' as string and return dict like below output.
#dict = {'p' : '###p###', 'y': '__y__', 't': '++t++', 'h': '??h??', 'o':'==0==', 'n':'**n**'}

str1 = 'python'
dict={}

for char in str1:
    if char == 'p':
        dict[char] = f"###{char}###"
    elif char == 'y':
        dict[char] = f"__{char}__"
    elif char == 't':
        dict[char] = f"++{char}++"
    elif char == 'h':
        dict[char] = f"??{char}??"
    elif char == 'o':
        dict[char] = f"=={char}=="
    elif char == 'n':
        dict[char] = f"**{char}**"

print(dict)