class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}: {current_question.text} "
                            f"(True or False?) ")

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You are right. Your core is: {self.score}/{self.question_number}")
        else:
            print(f"You are wrong. Your core is: {self.score}/{self.question_number}")
        print(f"Correct answer: {correct_answer}")

