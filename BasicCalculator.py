def calculator(num1,num2,op):
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        print(num1/num2)
    else:
        print("Choose the right operator")



num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
op=input("Enter the operator: ( + , - , / , *)")
calculator(num1,num2,op)
