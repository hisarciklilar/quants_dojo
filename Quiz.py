class Quiz:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list


    def quiz_continue(self, usr_response):
        print("start end quiz")
        print(self.question_number)
        print(len(self.question_list))
        if usr_response.lower() == "quit":
            return False
        elif self.question_number < len(self.question_list):
            return True
        else: 
            return False


    def reveal_question(self):
        question_to_reveal = self.question_list[self.question_number]["question"]
        self.question_number += 1
        print(f"Q.{self.question_number}: True or False?\n")
        user_response = input(f"'{question_to_reveal}' (T/F)\n")
        return user_response

