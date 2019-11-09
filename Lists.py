foods=["pizza","pasta","cake"]
print(foods[1])

#lists can have elements of different data types
list=["Samuel",90,False,"soren",900,True]

print(list)

#Accessing elements of lists in different ways
print(list[-2])
print(list[1:])
print(list[1:3])

#changing elements of lists
list[2]="chicken"

print(list)

listName=["Ginny","Ron","Fred","George","Bill","Charles","Percy"]
print(listName)

listAge=[12,13,15,16,17,20,22]
print(listAge)

#Adding one list to another list
foods.extend(list)

#Adding an element to the end of a list
listName.append("Harry")

#Adding an element to any position of a list
listName.insert(-2,"Hermoine")

#Removing elements from a list
listAge.remove(13)

#clearing a list
list.clear()

#popping an element from a list
listName.pop()

#To find if a specific element is in a list
print(listName.index("Bill"))

#counting a specific element in a list
print(listName.count("Ginny"))

#sorting a list
listName.sort()
print(listName)

#reversing a list
print(listAge.reverse())

#copying a list
listAge2=listAge.copy()
print(listAge)
print(listAge2)

print(listName)
print(listAge)
print(list)

