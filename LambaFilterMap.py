#Map function

def convert_to_even(oddNumber):
    return  oddNumber + 1

oddNumberList = [1,3,5,7,9]

evenNumber = list(map(convert_to_even,oddNumberList))
print(evenNumber)

for item in map(convert_to_even,oddNumberList):
    print(item)

#Filter function

def check_even(number):
    return number%2==0
numberList=[1,2,3,4,5,6,7,8]
evenList=list(filter(check_even,numberList))
print(evenList)

for item in filter(check_even,numberList):
    print(item)

#Lambda Expressions
lambda oddNumber:oddNumber + 1

#lambda with map and filter

mapList = list(map(lambda oddNumber:oddNumber + 1,oddNumberList))
print(mapList)

filterList = list(filter(lambda number:number%2==0,numberList))
print(filterList)

namesList = ["Andy","Sandy","Mandy"]

mapNamesList = list(map(lambda item:item[0].upper(),namesList))
print(mapNamesList)