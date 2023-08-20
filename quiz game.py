import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import random

# questions
questions = [
    {
        "question": "who developed python programming language?",
        "choices": ["wick van rossum", "rasmus lerdorf", "Guido van rossum", "Niene stom"],
        "correct_answer": "Guido van rossum",
    },
    {
        "question": "Which of the following is used to define a block of code in python?",
        "choices": ["Indentation", "key", "Brackets", "all of the mentioned"],
        "correct_answer": "Indentation",
    },
    {
        "question": "what does pip stand for python?",
        "choices": ["pip Installs Python", " pip Installs Packages", "Preferred Installer Program", "All of the mentioned"],
        "correct_answer": "Preferred Installer Program",
    },
    {
        "question": 'Which of the following statements is used to create an empty set in Python?',
        "choices": [
            "()",
            "{}",
            "[]",
            "set()",
        ],
        "correct_answer": "set()",
    },
]


class QuizGame:
    def __init__(self, root):
        self.root = root
        self.score = 0
        self.questions_copy = questions.copy()
        self.current_question = None
        self.selected_button = None

        self.question_label = tk.Label(
            root,
            text="",
            wraplength=400,
            font=Font(family="white", size=14, weight="bold"),
            bg="black",
            fg="silver",
        )
        self.question_label.pack(pady=20)

        self.choices_buttons = []
        for _ in range(4):
            button = tk.Button(
                root,
                text="",
                width=30,
                font=Font(family="white", size=12),
                bg="black",
                fg="silver",
                activebackground="white",
            )
            button.pack(pady=5)
            self.choices_buttons.append(button)

        self.answer_label = tk.Label(
            root,
            text="",
            wraplength=400,
            font=Font(family="white", size=14, weight="bold"),
            bg="black",
            fg="silver",
        )
        self.answer_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if len(self.questions_copy) > 0:
            self.current_question = random.choice(self.questions_copy)
            self.question_label.config(text=self.current_question["question"])

            choices = self.current_question["choices"]
            random.shuffle(choices)

            for i, button in enumerate(self.choices_buttons):
                button.config(text=choices[i])
                button.config(command=lambda b=button: self.button_selected(b))
                button.config(state="normal")

            self.selected_button = None
            self.answer_label.config(text="")
        else:
            self.show_results()

    def button_selected(self, button):
        self.selected_button = button
        self.check_answer()

    def check_answer(self):
        if self.selected_button is not None:
            user_answer = self.selected_button["text"]
            correct_answer = self.current_question["correct_answer"]

            if user_answer == correct_answer:
                self.score += 1
                self.answer_label.config(text="Your answer is correct!", fg="green")
            else:
                self.answer_label.config(
                    text=f"Your answer is incorrect!\nThe correct answer is: {correct_answer}",
                    fg="red",
                )

            self.selected_button.config(state="disabled")
            self.questions_copy.remove(self.current_question)
            self.root.after(1000, self.next_question)

    def show_results(self):
        result_text = f"Final Score: {self.score}/{len(questions)}"
        self.answer_label.config(text=result_text, fg="green")

        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.score = 0
            self.questions_copy = questions.copy()
            random.shuffle(self.questions_copy)
            self.next_question()
        else:
            self.root.destroy()


root = tk.Tk()
root.title("Quiz Game")
root.geometry("600x500")
root.configure(bg="black")
game = QuizGame(root)
root.mainloop()
