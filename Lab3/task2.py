import tkinter as tk
from tkinter import filedialog, messagebox

# Таблиця відповідності символів
alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
alphabet_numbers = {char: i for i, char in enumerate(alphabet)}

def select_file(title):
    file_path = filedialog.askopenfilename(title=title, filetypes=[("Text files", "*.txt")])
    return file_path

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def decrypt(text, password):
    decrypted_text = []
    for i, char in enumerate(text):
        if char in alphabet_numbers:
            text_index = alphabet_numbers[char]
            password_char = password[i % len(password)]
            password_index = alphabet_numbers[password_char]
            decrypted_index = (text_index - password_index) % len(alphabet)
            decrypted_text.append(alphabet[decrypted_index])
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def decrypt_file():
    file2_path = select_file("Виберіть Прізвище2.txt")
    file3_path = select_file("Виберіть Прізвище3.txt")
    file4_path = filedialog.asksaveasfilename(title="Зберегти Прізвище4.txt", defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if not file2_path or not file3_path or not file4_path:
        messagebox.showwarning("Увага", "Потрібно вибрати всі файли!")
        return

    password = read_file(file2_path).strip()
    encrypted_text = read_file(file3_path)

    if len(password) < 10:
        messagebox.showwarning("Увага", "Пароль має бути не менше 10 символів!")
        return

    decrypted_text = decrypt(encrypted_text, password)
    write_file(file4_path, decrypted_text)
    messagebox.showinfo("Успіх", "Текст успішно дешифровано та збережено.")

root = tk.Tk()
root.title("Лабораторна робота 3")

btn_decrypt_files = tk.Button(root, text="Дешифрувати файли", command=decrypt_file)
btn_decrypt_files.pack(pady=20)

root.mainloop()
