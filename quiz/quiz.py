import os

class Quiz:

    def __init__(self, question_list):
        self.question_index = 0
        self.question_list = question_list
        self.response = ""
        self.score = 0 
        self.question_progress = True
        self.score_list=[]

    def clear_terminal(self):
        input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

    def end_of_quiz(self):
        if self.question_index >= len(self.question_list) or self.response.lower() == "quit":
            print("end of quiz!")
            return True

    def reveal_question(self):
        while self.question_progress:
            self.clear_terminal()
            question_to_reveal = self.question_list[self.question_index]["question"]
            print(f"Q.{self.question_index + 1}: True or False?\n \n")
            self.response = input(f"'{question_to_reveal}' (True/False)\n \n")
            self.check_answer()
        
        self.question_progress = True
        self.question_index += 1
    

    def check_answer(self):
        valid_answers = ["true", "false"]
        correct_answer = self.question_list[self.question_index]["answer"]
        if self.response.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct! \n \n  The answer was {correct_answer}\n \n")
            print(f"You have answered {self.score} out of {self.question_index +1} questions correctly. \n \n")
            print(f"Your current score is {round((self.score / (self.question_index + 1))*100, 2)}% \n \n")   
            self.track_score(1)
            self.question_progress = False 
        elif self.response.lower() == "quit":
            print("You chose to quit the session.")
            self.question_progress = False
        elif self.response.lower() not in valid_answers:
            print("Value Error: You need to type either 'true' or 'false'. Please try again. \n")
        else:
            print(f"This is incorrect.\n \n  The answer was {correct_answer}\n \n")
            print(f"You have answered {self.score} out of {self.question_index +1} questions correctly. \n \n")
            print(f"Your current score is {round((self.score / (self.question_index + 1))*100, 2)}% \n \n")    
            self.track_score(0)
            self.question_progress = False

    def track_score(self,scr):
        self.score_list.append(scr)
