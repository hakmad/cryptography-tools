def rot13(ciphertext, shift):
    text = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord("A") - shift) % 26
                    + ord("A"))
            elif char.islower():
                new_char = chr((ord(char) - ord("a") - shift) % 26
                    + ord("a"))
        else:
            new_char = char

        text += new_char

    return text

def rot47(ciphertext, shift):
    text = ""

    for char in text:
        if char.isascii() and not(char.isspace()):
            new_char = chr((ord(char) - ord("!") - shift) % 94 + ord("!"))
        else:
            new_char = char

        text += new_char

    return text
