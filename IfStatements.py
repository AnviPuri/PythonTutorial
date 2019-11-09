def functionDemo(isMale,isHappy):
    if isMale or isHappy:
        print("You are male or Happy!")
    else:
        print("You are neither male nor Tall!")

    if isMale and isHappy:
        print("You are a tall male")
    elif isMale and not(isHappy):
        print("You are an unhappy male")
    elif not(isMale) and isHappy:
        print("You are happy but not a male")
    else:
        print("You are either not male or not tall or both")

def max_num(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

isMale= True
isHappy=False
functionDemo(isMale,isHappy)

print("The greatest number is: " + str(max_num(3,4,5)))