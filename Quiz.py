class Quiz:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def reveal_question(self):
        question_to_reveal = self.question_list[self.question_number]["question"]
        self.question_number += 1
        print(f"Q.{self.question_number}: True or False?\n")
        user_response = input(f"'{question_to_reveal}' (T/F)\n")
        return user_response
