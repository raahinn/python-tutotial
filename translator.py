# AEIOUaeiou this letters will be translated into g

def translator(phrase):
    print(f'The phrase is {phrase}')
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase: ")))