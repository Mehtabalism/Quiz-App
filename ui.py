from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, font=("Arial", 10, "italic"), text="Place Question Here", width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score.grid(column=1, row=0)

        correct_img = PhotoImage(file="./images/true.png")
        self.correct = Button(image=correct_img, highlightthickness=0, borderwidth=0, command=self.is_true)
        self.correct.grid(column=1, row=2)
        incorrect_img = PhotoImage(file="./images/false.png")
        self.incorrect = Button(image=incorrect_img, highlightthickness=0, borderwidth=0, command=self.is_false)
        self.incorrect.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.correct["state"] = NORMAL
            self.incorrect["state"] = NORMAL
            self.canvas.config(bg="white")
            self.score["text"] = f"Score: {self.quiz.score}"
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.correct["state"] = DISABLED
            self.incorrect["state"] = DISABLED

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.correct["state"] = DISABLED
        self.incorrect["state"] = DISABLED
        self.window.after(1000, self.get_next_question)

