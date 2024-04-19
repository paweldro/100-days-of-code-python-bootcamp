from tkinter import *
from quiz_brain import Quiz

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: Quiz):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 15, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, fill="black",
                                                     font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_button_on_click)
        self.false_button.grid(row=2, column=1)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_button_on_click)
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_question():
            self.false_button.config(state="normal")
            self.true_button.config(state="normal")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def give_feedback(self, user_answer):
        if self.quiz.check_answer(user_answer):
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, func=self.get_next_question)

    def false_button_on_click(self):
        self.false_button.config(state="disabled")
        self.true_button.config(state="disabled")
        self.give_feedback(user_answer="False")

    def true_button_on_click(self):
        self.false_button.config(state="disabled")
        self.true_button.config(state="disabled")
        self.give_feedback(user_answer="True")

