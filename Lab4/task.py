import tkinter as tk
from tkinter import filedialog, messagebox

def save_questions():
    questions = [entry_question1.get(), entry_question2.get(), entry_question3.get(), entry_question4.get(), entry_question5.get()]
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            for question in questions:
                file.write(question + '\n')
        messagebox.showinfo("Success", "Запитання успішно збережені")

def load_questions():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            questions = file.readlines()
        if len(questions) >= 5:
            entry_question1.delete(0, tk.END)
            entry_question1.insert(0, questions[0].strip())
            entry_question2.delete(0, tk.END)
            entry_question2.insert(0, questions[1].strip())
            entry_question3.delete(0, tk.END)
            entry_question3.insert(0, questions[2].strip())
            entry_question4.delete(0, tk.END)
            entry_question4.insert(0, questions[3].strip())
            entry_question5.delete(0, tk.END)
            entry_question5.insert(0, questions[4].strip())
        messagebox.showinfo("Success", "Запитання успішно завантажені")

def save_answers():
    answers = [entry_answer1.get(), entry_answer2.get(), entry_answer3.get(), entry_answer4.get(), entry_answer5.get()]
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            for answer in answers:
                file.write(answer + '\n')
        messagebox.showinfo("Success", "Відповіді успішно збережені")

def load_answers():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            answers = file.readlines()
        if len(answers) >= 5:
            entry_answer1.delete(0, tk.END)
            entry_answer1.insert(0, answers[0].strip())
            entry_answer2.delete(0, tk.END)
            entry_answer2.insert(0, answers[1].strip())
            entry_answer3.delete(0, tk.END)
            entry_answer3.insert(0, answers[2].strip())
            entry_answer4.delete(0, tk.END)
            entry_answer4.insert(0, answers[3].strip())
            entry_answer5.delete(0, tk.END)
            entry_answer5.insert(0, answers[4].strip())
        messagebox.showinfo("Success", "Відповіді успішно завантажені")

root = tk.Tk()
root.title("Програма для передачі запитань колегам з групи")

tk.Label(root, text="Питання 1").grid(row=0, column=0)
tk.Label(root, text="Відповідь 1").grid(row=1, column=0)
tk.Label(root, text="Питання 2").grid(row=2, column=0)
tk.Label(root, text="Відповідь 2").grid(row=3, column=0)
tk.Label(root, text="Питання 3").grid(row=4, column=0)
tk.Label(root, text="Відповідь 3").grid(row=5, column=0)
tk.Label(root, text="Питання 4").grid(row=6, column=0)
tk.Label(root, text="Відповідь 4").grid(row=7, column=0)
tk.Label(root, text="Питання 5").grid(row=8, column=0)
tk.Label(root, text="Відповідь 5").grid(row=9, column=0)

entry_question1 = tk.Entry(root, width=50)
entry_question1.grid(row=0, column=1)
entry_answer1 = tk.Entry(root, width=50)
entry_answer1.grid(row=1, column=1)
entry_question2 = tk.Entry(root, width=50)
entry_question2.grid(row=2, column=1)
entry_answer2 = tk.Entry(root, width=50)
entry_answer2.grid(row=3, column=1)
entry_question3 = tk.Entry(root, width=50)
entry_question3.grid(row=4, column=1)
entry_answer3 = tk.Entry(root, width=50)
entry_answer3.grid(row=5, column=1)
entry_question4 = tk.Entry(root, width=50)
entry_question4.grid(row=6, column=1)
entry_answer4 = tk.Entry(root, width=50)
entry_answer4.grid(row=7, column=1)
entry_question5 = tk.Entry(root, width=50)
entry_question5.grid(row=8, column=1)
entry_answer5 = tk.Entry(root, width=50)
entry_answer5.grid(row=9, column=1)

btn_save_questions = tk.Button(root, text="Зберегти питання", command=save_questions)
btn_save_questions.grid(row=10, column=0, pady=10)
btn_load_questions = tk.Button(root, text="Відкрити питання", command=load_questions)
btn_load_questions.grid(row=10, column=1, pady=10)
btn_save_answers = tk.Button(root, text="Зберегти відповіді", command=save_answers)
btn_save_answers.grid(row=11, column=0, pady=10)
btn_load_answers = tk.Button(root, text="Відкрити відповіді", command=load_answers)
btn_load_answers.grid(row=11, column=1, pady=10)

root.mainloop()
