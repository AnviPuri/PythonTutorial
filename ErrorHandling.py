num_one = int(input("Enter the first number"))
num_two = int(input("Enter the first number"))

try:
    result = num_one / num_two
except:
    print("An exception occured. Try again!")
else:
    print(result)
finally:
    print("END OF PROGRAM")


