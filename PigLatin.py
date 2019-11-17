def pig_latin(word,pigLatinSuffix):
    firstLetter = word[0].lower()
    if firstLetter in "aeiou":
        newWord = word + pigLatinSuffix
    else:
        newWord = word[1:] + firstLetter + pigLatinSuffix
    return newWord

word=input("Enter a word")
pigLatinSuffix=input("Enter your pig latin suffix")
print(f"The word in pig latin is {pig_latin(word,pigLatinSuffix)}")