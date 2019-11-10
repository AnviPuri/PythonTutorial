#volwels->#
#consonants->$

def translate(phrase):
    translatedPhrase=""
    for letter in phrase.lower():
        if letter.lower() in "aeiou":
            translatedPhrase = translatedPhrase + "#"
        else:
            translatedPhrase = translatedPhrase + "$"
    return translatedPhrase

print(translate("My name is BULBA"))