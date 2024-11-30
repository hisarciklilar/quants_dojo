import os
# import quiz.quiz
import quiz.assets.logo as logo
# from quiz.assets.question_bank import question_list
# import quiz.quiz_generator
from user_database.user_database import UserDatabase

user = UserDatabase()

# def clear_terminal_start():
#     # input("Press enter if you dare!\n")
    
#     os.system('cls' if os.name == 'nt' else 'clear')
#     return user_id 

def validate_user_id(id):
    try: 
        user.user_id = int(id)
        if len(id) != 3:
            raise ValueError(f"User id does not exist. Your user id should consist of 3 digits\n")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def start_quiz():
    # user_id_verified = False
    # while not user_id_verified:
    print(logo.logo_picture)
    print("Welcome to Quants Dojo!\n")
    print("Ready to test your Econometrics skills? \n")
    while True:
        user_id_str = input("Type your user id below and continue to the quiz if you dare!\n")
        if validate_user_id(user_id_str):
            print("User id typed as expected")
            break


def quiz_info():
    print(logo.logo_title)
    print("This challenge includes 10 True/False questions.\n")
    print("Your task is to find the correct answer and type either 'true' or 'false' in terminal.\n")
    print("You may type 'quit' to quit the quiz anytime.\n")



def quiz_start():
    start_quiz()
    quiz_info()