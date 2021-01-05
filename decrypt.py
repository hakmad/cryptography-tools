def rot13(text, shift):
    new_text = ""

    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                new_letter = chr((ord(letter) - ord("A") - shift) % 26
                    + ord("A"))
            elif letter.islower():
                new_letter = chr((ord(letter) - ord("a") - shift) % 26
                    + ord("a"))
        else:
            new_letter = letter

        new_text += new_letter

    return new_text

def rot47(text, shift):
    new_text = ""

    for letter in text:
        if letter.isascii() and not(letter.isspace()):
            new_letter = chr((ord(letter) - ord("!") - shift) % 94 + ord("!"))
        else:
            new_letter = letter

        new_text += new_letter

    return new_text
