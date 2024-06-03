def caesar_cipher(text, shift):
    result = ""
    # Визначення алфавіту для великих та малих літер
    alphabet_upper = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯABC'
    alphabet_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяd'
    alphabet_length = len(alphabet_upper)

    # Шифрування кожного символу
    for char in text:
        if char.isalpha():
            if char in alphabet_upper:
                idx = alphabet_upper.index(char)
                new_char = alphabet_upper[(idx + shift) % alphabet_length]
            elif char in alphabet_lower:
                idx = alphabet_lower.index(char)
                new_char = alphabet_lower[(idx + shift) % alphabet_length]
            else:
                new_char = char
            result += new_char
        else:
            result += char
    return result

