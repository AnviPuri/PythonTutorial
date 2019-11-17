def find_sum(numberList):
    check = False
    sum = 0
    for i in numberList:
        if i == 6:
            check = True
        if(not(check)):
            sum = sum + i
        if i == 9:
            check = False
    return sum

print(find_sum([2, 1, 6, 9, 11]))
