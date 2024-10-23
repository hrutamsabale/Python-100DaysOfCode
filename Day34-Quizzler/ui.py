import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="SOME", font=("arial", 20, "italic"), fill=THEME_COLOR,
                                                width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.tick_img = tkinter.PhotoImage(file="../../Python-100DaysOfCode/Day35-Quizzler/images/true.png")
        self.cross_img = tkinter.PhotoImage(file="../../Python-100DaysOfCode/Day35-Quizzler/images/false.png")

        self.right_button = tkinter.Button(image=self.tick_img, highlightthickness=0, pady=20, padx=20,
                                           command=self.true_pressed)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = tkinter.Button(image=self.cross_img, highlightthickness=0, pady=20, padx=20,
                                           command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.canvas.itemconfig(self.question, text=f"That's the end of it!")

    def update_scoreboard(self):
        self.score_label.config(text=f"Score: {self.score}")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.update_scoreboard()
        self.window.after(500, self.get_next_question)
