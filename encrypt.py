def rot13(text, shift):
    ciphertext = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord("A") + shift) % 26
                    + ord("A"))
            elif char.islower():
                new_char = chr((ord(char) - ord("a") + shift) % 26
                    + ord("a"))
        else:
            new_char = char

        ciphertext += new_char

    return ciphertext

def rot47(text, shift):
    ciphertext = ""

    for char in text:
        if char.isascii() and not(char.isspace()):
            new_char = chr((ord(char) - ord("!") + shift) % 94 + ord("!"))
        else:
            new_char = char

        ciphertext += new_char

    return ciphertext

def xor_string(text, key):
    ciphertext = ""

    key = (key * (len(text) // len(key) + 1))[:len(text)]

    for text_char, key_char in zip(text, key):
        ciphertext += chr(ord(text_char) ^ ord(key_char))

    return ciphertext

def xor_numeric(text, key):
    ciphertext = ""

    for char in text:
        ciphertext += chr(ord(char) ^ key)

    return ciphertext
