import tkinter as tk
from tkinter import filedialog

def create_empty_files():
    open('Прізвище1.txt', 'w').close()
    open('Прізвище2.txt', 'w').close()
    open('Прізвище3.txt', 'w').close()
    tk.messagebox.showinfo("Success", "Порожні файли були створені.")

root = tk.Tk()
root.title("Лабораторна робота 3")

btn_create_files = tk.Button(root, text="Створити порожні файли", command=create_empty_files)
btn_create_files.pack()

root.mainloop()
