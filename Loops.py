#while loop
i = 1

while i <= 10:
    print(i)
    i=i+1

print("Outside the loop")

#for loop
array= [1,2,3,4,"Jamaica"]

for i in array:
    print(i)

for j in "Miami":
    print(j)

for index in range(10):
    print(index)

for index in range(10,20):
    print(index)

for index in range(len(array)):
    print(array[index])

#2D Lists and nested loops
#2D lists
numberSets=[
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

print(numberSets[0][0]+numberSets[1][1]+numberSets[2][2])

#nested loops
for row in numberSets:
    print(row)

for row in numberSets:
    for col in row:
        print(col)

