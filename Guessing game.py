def guessWord(secretWord):
    chance=3
    i=0
    lastChance = chance-1
    responseWord=""
    while i<chance:
        responseWord=input("Guess the word")
        if responseWord == secretWord:
            print("You guessed it right!")
            break
        else:
            if i == lastChance:
                print("Sorry you lose :(")
            else:
                print("Try again!")
        i=i+1

secretWord = input("Enter a secret word")
guessWord(secretWord)
