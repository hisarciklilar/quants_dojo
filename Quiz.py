class Quiz:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_response =""

    def end_of_quiz(self):
        if self.question_number >= len(self.question_list) or self.user_response.lower() == "quit":
            print("end of quiz!")
            return True


    def reveal_question(self):
        question_to_reveal = self.question_list[self.question_number]["question"]
        self.question_number += 1
        print(f"Q.{self.question_number}: True or False?\n")
        self.user_response = input(f"'{question_to_reveal}' (T/F)\n")
        print(self.user_response)

