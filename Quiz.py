import os

class Quiz:

    def __init__(self, question_list):
        self.question_index = 0
        self.question_list = question_list
        self.response = ""
        self.score = 0 

    def clear_terminal(self):
        input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

    def start_quiz(self):
        print("Welcome to Quants Dojo!\n\n")
        print("This is a place where you can test your Econometrics skills \n \n")
        print("Ready for the challenge?! \n\n")
        self.reveal_question()

    def end_of_quiz(self):
        if self.question_index >= len(self.question_list) or self.response.lower() == "quit":
            print("end of quiz!")
            return True

    def reveal_question(self):
        self.clear_terminal()
        question_to_reveal = self.question_list[self.question_index]["question"]
        print(f"Q.{self.question_index + 1}: True or False?\n \n")
        self.response = input(f"'{question_to_reveal}' (True/False)\n \n")
        self.check_answer()
        self.question_index += 1


    def check_answer(self):
        if self.response.lower() == self.question_list[self.question_index]["answer"].lower():
            self.score += 1
            print(f"Correct! \n \n  The answer was {self.question_list[self.question_index]["answer"]}\n \n")
        elif self.response.lower() == "quit":
            print("You chose to quit the session.")
        else:
            print(f"This is incorrect.\n \n  The answer was {self.question_list[self.question_index]["answer"]}\n \n")
        print(f"You have answered {self.score} out of {self.question_index +1} questions correctly. \n \n")
        print(f"Your current score is {round((self.score / (self.question_index + 1))*100, 2)}% \n \n")    
        