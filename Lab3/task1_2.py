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

def encrypt(text, password):
    encrypted_text = []
    for i, char in enumerate(text):
        if char in alphabet_numbers:
            text_index = alphabet_numbers[char]
            password_char = password[i % len(password)]
            password_index = alphabet_numbers[password_char]
            encrypted_index = (text_index + password_index) % len(alphabet)
            encrypted_text.append(alphabet[encrypted_index])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def encrypt_file():
    file1_path = select_file("Виберіть Прізвище1.txt")
    file2_path = select_file("Виберіть Прізвище2.txt")
    file3_path = filedialog.asksaveasfilename(title="Зберегти Прізвище3.txt", defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if not file1_path or not file2_path or not file3_path:
        messagebox.showwarning("Увага", "Потрібно вибрати всі файли!")
        return

    text = read_file(file1_path)
    password = read_file(file2_path).strip()

    if len(password) < 10:
        messagebox.showwarning("Увага", "Пароль має бути не менше 10 символів!")
        return

    encrypted_text = encrypt(text, password)
    write_file(file3_path, encrypted_text)
    messagebox.showinfo("Успіх", "Текст успішно зашифровано та збережено.")

root = tk.Tk()
root.title("Лабораторна робота 3")

btn_encrypt_files = tk.Button(root, text="Зашифрувати файли", command=encrypt_file)
btn_encrypt_files.pack(pady=20)

root.mainloop()
