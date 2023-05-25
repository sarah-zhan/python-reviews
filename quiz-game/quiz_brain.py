class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions

    def next_question(self):
        user_answer = input(f"Question {self.question_number}: {self.question_list[self.question_number].text} "
                            f"(True or False?)")
        return user_answer



