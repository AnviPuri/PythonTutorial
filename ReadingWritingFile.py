#Reading a file
namesFile=open("Names.txt", "r")
namesFileAppend=open("Names.txt", "a")
namesFileWrite=open("Age.txt","w")
print(namesFile.readable())
print(namesFile.readlines()[1])
print(namesFile.read())
for name in namesFile.readlines():
    print(name)
namesFile.close()

#Appending to a file
namesFileAppend.write("\nGrace")
namesFileAppend.close()

#Writing to a file
namesFileWrite.write("12")

