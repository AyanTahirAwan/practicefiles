#translator

def translate(phrase):
    result=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                result= result+"G"
            else:
                result= result+"g"

        else:
            result= result+letter
    return result

print(translate(input("Enter your phrase:  ")))