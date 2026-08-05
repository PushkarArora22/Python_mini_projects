def main():
    a=int(input("Enter first number:- "))
    b=int(input("Enter second number:- "))
    c=input("Enter operator(+,-,*,/):- ")
    print(f"Answer of {a} {c} {b} = {calculator(a,b,c)}")

def calculator(num1,num2,operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        if num2==0:
            return "Cannot divide by zero"
        return num1/num2
    else:
        return "Invalid operator"

main()
