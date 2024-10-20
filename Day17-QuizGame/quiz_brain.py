class QuizBrain:
    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0
    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        question = self.question_list[self.question_no]
        answer = input(f"Q.{self.question_no + 1}) {question.text} (True/False): ").lower()
        q_answer = question.answer.lower()
        self.check_answer(answer, q_answer)
        self.question_no += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print(f"That wrong. The correct answer was {correct_answer.capitalize()}")
        print(f"Your current score : {self.score}/{self.question_no + 1}\n")

