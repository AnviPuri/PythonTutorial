def printNameAge(name,age):
    print("Hi " + name + ". Are you really " + str(age) + "?")

def add(a,b):
    c=a+b
    return c


name=input("What is your name?")
age=input("What is your age?")
printNameAge(name,age)

a=int(input("Enter a number"))
b=int(input("Enter a number"))
print("The sum is " + str(add(a,b)))

