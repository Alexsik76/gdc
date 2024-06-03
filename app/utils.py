def caesar_cipher(text, shift):
    result = ""
    for char in text:
        print(char)
        if char.isalpha():
            if char in 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ':
                idx = ord(char) - ord('А')
                new_char = chr((idx + shift) % 33 + ord('А'))
            elif char in 'абвгґдеєжзииіїйклмнопрстуфхцчшщьюя':
                idx = ord(char) - ord('а')
                new_char = chr((idx + shift) % 33 + ord('а'))
            else:
                new_char = char
            result += new_char
        else:
            result += char
    return result

