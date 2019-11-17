def countPrime(number):
    count = 1
    start = 3
    if number<2:
        return 0
    while start <= number:
        for j in range(2,start):
            if (start%j) == 0:
                start = start+2
                break
        else:
            count = count + 1
            start = start + 2
    return count

number=int(input("Enter a number"))
count = countPrime(number)
print(f"{count} prime numbers between 0 and {number}")