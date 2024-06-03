def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            idx = ord(char)
            new_char = chr(idx + shift)
            result += new_char
        else:
            result += char
    return result

