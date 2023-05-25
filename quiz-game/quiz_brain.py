class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True

    def next_question(self):
        question_number_show = self.question_number + 1
        user_answer = input(f"Question {question_number_show}: {self.question_list[self.question_number].text} "
                            f"(True or False?) ")
        self.question_number += 1
        return user_answer



