class Quiz:

    def __init__(self, question_list):
        self.question_index = 0
        self.question_list = question_list
        self.response =""


    def end_of_quiz(self):
        if self.question_index >= len(self.question_list) or self.response.lower() == "quit":
            print("end of quiz!")
            return True


    def reveal_question(self):
        question_to_reveal = self.question_list[self.question_index]["question"]
        print(f"Q.{self.question_index + 1}: True or False?\n")
        self.response = input(f"'{question_to_reveal}' (True/False)\n")
        self.check_answer()
        self.question_index += 1

    def check_answer(self):
        if self.response.lower() == self.question_list[self.question_index]["answer"].lower():
            print(f"Correct! \n \n  The answer was {self.question_list[self.question_index]["answer"]}\n \n")
        else:
            print(f"This is incorrect.\n \n  The answer was {self.question_list[self.question_index]["answer"]}\n \n")