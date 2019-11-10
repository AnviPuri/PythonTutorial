def raisePower(number,power):
    result=1
    for i in range(power):
        result = result*number
    return result

number=float(input("Enter the number:"))
power=int(input("Enter the power:"))
print(raisePower(number,power))