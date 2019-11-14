from random import randint

#Sets
myFirstSet = set()

myFirstSet.add(1)
myFirstSet.add(2)
print(myFirstSet)

myFirstSet.add(1)
print(myFirstSet)

print(type(myFirstSet))

#Tuples
#Tuple unpacking
tupleList=[(1,2),(3,4),(5,6)]
for a,b in tupleList:
    print(a)
    print(b)

#enumerate method
for item in enumerate(tupleList):
    print(item)

for a,b in enumerate(tupleList):
    print(f"{a}-{b}")
    print(b[0])

#zip method
listNumber=[1,2,3]
listLetter=["a","b","c"]

for item in zip(listLetter,listNumber):
    print(item)

listCollect=list(zip(listLetter,listNumber))
print(listCollect)

#random library
print(randint(0,1000))





