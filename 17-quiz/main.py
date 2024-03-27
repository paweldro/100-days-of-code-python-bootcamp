from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []
for question in question_data:
    q = Question(question["text"], question["answer"])
    question_bank.append(q)

quiz = Quiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{len(quiz.question_list)}")
