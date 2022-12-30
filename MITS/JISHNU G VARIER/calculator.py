a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=1
while(c==1):
    print("Enter any one of these operators( + , - , * , / ): ")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    print("\n")
    d=input()
    if d=='+':
        print("Addition of numbers= ",(a+b))
    elif d=='-':
        print("Subtraction of numbers= ",(a-b))
    elif d=='*':
        print("Multiplication of numbers= ",(a*b))
    elif d=='/':
        print("Division of numbers= ",(a/b))
    else:
        print("Invalid operator")
    p=input("Do you want to continue the operations? say 'y' for YES or 'n' for NO...\n")
    if p=='y':
        c=1
    else:
        c=0
        print("Exited...")
