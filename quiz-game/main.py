from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# create question bank
question_bank = []

for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()
