import os
import quiz.assets.logo as logo
from user_database.user_database import UserDatabase


user = UserDatabase()

# def clear_terminal_start():
#     # input("Press enter if you dare!\n")
    
#     os.system('cls' if os.name == 'nt' else 'clear')
#     return user_id 


def validate_user_id(id):
    """
    Validates user's 'user id' input through checks on the length, type and presence in the user register list.
    """
    valid_user_id_list = user.call_user_id_list()
    try: 
        user_id = int(id)
        if len(id) != 3:
            raise ValueError(f"User id does not exist. Your user id should be combination of 3 numbers\n")
        if user_id not in valid_user_id_list:
            raise ValueError(f"User id is not found in list of users \n If you do not have a registered user id, use 999 \n Your progress will not be recorded in this instance")      
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def start_quiz():
    """
    Asks for 'user id' in a welcome screen.
    """
    print(logo.logo_picture)
    print("Welcome to Quants Dojo!\n")
    print("Ready to test your Econometrics skills? \n")
    while True:
        user_id_str = input("Type your user id below and continue to the quiz if you dare!\n")
        if validate_user_id(user_id_str):
            print("User id recorded. Starting the quiz...")
            return user_id_str
            

def quiz_info():
    """
    Display quiz information
    """
    print(logo.logo_title)
    print("This challenge includes 10 True/False questions.\n")
    print("Your task is to find whether the statement provided is 'true' or 'false'.\n")
    print("Type: 'true' (without the quotation mark) if you think the statement is true.\n")
    print("Type: 'false' (without the quotation mark) if you think the statement is false.\n")
    print("Type: 'quit' if you want to quit the quiz half-way through\n")


def quiz_start():
    """
    Returns 'user id' input by running quiz start and info functions
    """
    user_id_str = start_quiz()
    quiz_info()
    return user_id_str
    