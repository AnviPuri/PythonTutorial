try:
    value=10/1
    number=int(input("Enter s number:"))
    print(number)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)
