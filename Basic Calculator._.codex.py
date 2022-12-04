"""
Name -Jyotiranjan Mahapatra
Reg. no - 2241013013
telegram username - @Bapun_it_is
"""



def main11():
    try:
        print("select operator :\n+  [addition]\n-  [substraction]\n*  [multiplication]\n/  [division]\n^  [power]\n")
        a = input(":----  ")
        if a == "+":
            b = float(input("enter 1st number:--"))
            c = float(input("enter 2nd number:--"))
            ans = b + c
            print("your ans is ",ans)
        elif a == "-":
            b = float(input("enter 1st number:--"))
            c = float(input("enter 2nd number:--"))
            ans = b - c
            print("your ans is ",ans)
        elif a  == "*":
            b = float(input("enter 1st number:--"))
            c = float(input("enter 2nd number:--"))
            ans = b * c
            print("your ans is ",ans)
        elif a  == "/":
            b = float(input("enter 1st number:--"))
            c = float(input("enter 2nd number:--"))
            ans = b / c
            print("your ans is ",ans)
        elif a =="^":
            ans = 1
            b = float(input("enter 1st number:--"))
            c = int(input("enter power:--"))
            for i in range(0,c):
                ans  = ans * b
            print("your ans is",ans)
        else:
            print("error in typing")
    except Exception as e:
        print("invlid input")
    return ans
ans = main11()

    
def operator2(ans):
    try:
        print("select operator :\n+\n-\n*\n/\n^\n")
        a = input(":----  ")
        b = float(input("enter number:--"))
        if a == "+":
            ans = ans + b
            print("now,your new answer is ",ans)
        elif a == "-":
            ans = ans - b
            print("now,your new answer is ",ans)
        elif a  == "*":
            ans = ans * b
            print("now,your new answer is ",ans)
        elif a  == "/":
            ans = ans / b
            print("now,your new answer is ",ans)
        elif a =="^":
            z = int(b)
            ans1 = ans
            for i in range(0,z-1):
                ans  = ans * ans1
            print("now,your new answer is ",ans)
        else:
            print("error in typing ")
    except Exception as e:
        print("invalid input")
    return ans
while(1):
    try:
        print("press \"a\" for calculation with 'ANS'     and press    \"f\" for     'AC'    and \"b\" for break")
        cont = input()
        if cont=="a":
            print("your answer was ",ans)
            s = operator2(ans)
            ans = s+0
        elif cont == "f":
            main11()
        elif cont == "b":
            break
        else:
            print("invalid input")
    except Exception as e:
        print("invalid input try again once")
    
    
    
            
        
        
















































