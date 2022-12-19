def translate(phrase):
    translation= ""
    for leter in phrase:
        if leter.lower() in "aeiou":
           if leter.isupper():
                translation = translation + "G"
           else:
               translation + "g"
        else:
            translation = translation + leter
    return translation

print(translate(input("Enter a phrase: ")))