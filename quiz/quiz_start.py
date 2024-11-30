import os
# import quiz.quiz
import quiz.assets.logo as logo
# from quiz.assets.question_bank import question_list
# import quiz.quiz_generator

def clear_terminal_start():
    # input("Press enter if you dare!\n")
    user_id = input("Type your user id below and continue to the quiz if you dare!\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    return user_id 

def start_quiz():
    print(logo.logo_picture)
    print("Welcome to Quants Dojo!\n")
    print("Ready to test your Econometrics skills? \n")
    user_id = clear_terminal_start()
    return user_id

def quiz_info():
    print(logo.logo_title)
    print("This challenge includes 10 True/False questions.\n")
    print("Your task is to find the correct answer and type either 'true' or 'false' in terminal.\n")
    print("You may type 'quit' to quit the quiz anytime.\n")


def quiz_start():
    user_id = start_quiz()
    quiz_info()
    return user_id 