
def main11():
    print("select operator :\n+\n-\n*\n/\n^\n")
    a = input(":----  ")
    if a == "+":
        b = int(input("enter 1st number:--"))
        c = int(input("enter 2nd number:--"))
        ans = b + c
        print(ans)
    elif a == "-":
        b = int(input("enter 1st number:--"))
        c = int(input("enter 2nd number:--"))
        ans = b - c
        print(ans)
    elif a  == "*":
        b = int(input("enter 1st number:--"))
        c = int(input("enter 2nd number:--"))
        ans = b * c
        print(ans)
    elif a  == "/":
        b = int(input("enter 1st number:--"))
        c = int(input("enter 2nd number:--"))
        ans = b / c
        print(ans)
    elif a =="^":
        ans = 1
        b = int(input("enter 1st number:--"))
        c = int(input("enter 2nd number:--"))
        for i in range(0,c):
            ans  = ans * b
        print(ans)
    else:
        print("error in typing")

    return ans
ans = main11()

    
def operator2(ans):
    print(ans)
    print("select operator :\n+\n-\n*\n/\n^\n")
    a = input(":----  ")
    b = int(input("enter number:--"))
    if a == "+":
        ans = ans + b
        print(ans)
    elif a == "-":
        ans = ans - b
        print(ans)
    elif a  == "*":
        ans = ans * b
        print(ans)
    elif a  == "/":
        ans = ans / b
        print(ans)
    elif a =="^":
        ans1 = ans
        for i in range(0,b):
            
            ans  = ans * ans1
        print(ans)
    else:
        print("error in typing ")
    return ans
while(1):
    print("press \"a\" for     'ANS'     and press    \"f\" for     'AC'    and \"b\" for restart")
    cont = input()
    if cont=="a":
        s = operator2(ans)
        ans = s+0
    elif cont == "f":
        main11()
    else:
        break
    
    
    
            
        
        
















































