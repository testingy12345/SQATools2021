#4. Create a simple calculator which has option add, multiply, substract and divide

#each action should be calculated via function and ask user which action he wants to perform ,

#1. Addition
#2. Mulitplication
#3 Substraction
#4 Divide

#as per user choice calculate the stuff
# This function adds two numbers
def add(a,b):
    return a+b

# This function substraction two numbers
def sub(a,b):
    return a-b

# This function mul two numbers
def mul(a,b):
    return a*b

# This function division two numbers
def div(a,b):
    return a/b

print("Select Operation")
print("1. Add")
print("2. Substraction")
print("3. Multiply")
print("4. Division")

while True:
    choice= input("Enter choice(1/2/3/4) : ")
    # Check if choice is one of the four options
    if choice in ('1','2','3','4'):
        num1=float(input("Enter 1st no : "))
        num2=float(input("Enter 2nd no : "))

        if choice == '1':
            print(num1, "+" ,num2,"=" ,add(num1,num2))
        elif choice == '2':
                print(num1, "-", num2, "=", sub(num1, num2))
        elif choice == '3':
                print(num1, "*", num2, "=", mul(num1, num2))
        elif choice == '4':
                print(num1, "/", num2, "=", div(num1, num2))
        break
    else:
        print("Invalid input")