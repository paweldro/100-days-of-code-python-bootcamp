from question_model import Question
from data import question_data
from quiz_brain import Quiz
from ui import QuizInterface
question_bank = []
for question in question_data:
    q = Question(question["question"], question["correct_answer"])
    question_bank.append(q)

quiz = Quiz(question_bank)

quiz_ui = QuizInterface(quiz)

