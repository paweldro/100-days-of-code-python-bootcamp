class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True"
                            f"/False)?:")
        if user_answer.lower() != "false" and user_answer.lower() != "true":
            print("Wrong answer format. Answer only True/False!")
            print()

        else:
            self.check_answer(user_answer, self.question_list[self.question_number].answer)
            self.question_number += 1

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is: {self.score}/{len(self.question_list)}")
        print("\n")
