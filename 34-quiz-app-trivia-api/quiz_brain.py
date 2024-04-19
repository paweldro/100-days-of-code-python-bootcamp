import html


class Quiz:
    def __init__(self, q_list):
        self.current_question = None
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        if self.still_has_question():
            self.current_question = self.question_list[self.question_number]
            q_text = f"Q.{self.question_number + 1}: {html.unescape(self.current_question.text)}"
            self.question_number += 1
            return q_text                                                           

    def check_answer(self, user_answer: str) -> bool:
        if user_answer == self.current_question.answer:
            self.score += 1
            return True
        else:
            return False

