myfile = open('Names.txt')

#reading the file
fileContent=myfile.read()
print(fileContent)

#Bringing the cursor back to 0
myfile.seek(0)

fileContent=myfile.read()
print(fileContent)

#reading the file line by line
myfile.seek(0)
fileContent=myfile.readlines()
for i in fileContent:
    print(i)


#closing a file
myfile.close()

#another way to use a file
with open("Age.txt","r") as myAgeFile:
    content=myAgeFile.read()
print(content)

#Appending to a file
with open("Books.txt","a") as myBookFile:
    myBookFile.write("\nHarry Potter")

with open("Books.txt", "r") as myBookFile:
    myBookFile.seek(0)
    bookContent=myBookFile.read()

print(bookContent)

#Writing to a file
#Writing overwrites a file or creates a new file
with open("Names.txt","w") as myNameFile:
    myNameFile.write("All content Deleted")

with open("Names.txt","r") as myNameFile:
    myNameFile.seek(0)
    nameContent=myNameFile.read()

print(nameContent)
