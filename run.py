# import gspread
# from google.oauth2.service_account import Credentials
import os
import quiz.quiz
import quiz.assets.logo as logo
from quiz.assets.question_bank import question_list
import quiz.quiz_generator
import quiz.quiz_start as quiz_start
from user_database.user_database import UserDatabase

QUIZ_LENGTH = 10

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file("creds.json")
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open("quants_dojo")


# Generate quiz
quiz_generator = quiz.quiz_generator.QuizGenerator(question_list,QUIZ_LENGTH)
quiz_question_list = quiz_generator.generate_quiz()

# Start quiz
# quiz_start.quiz_start()
def clear_terminal_start():
    input("Press enter if you dare!\n")
    os.system('cls' if os.name == 'nt' else 'clear')

def start_quiz():
    print(logo.logo_picture)
    print("Welcome to Quants Dojo!\n")
    print("Ready to test your Econometrics skills? \n")
    clear_terminal_start()

def quiz_info():
    print(logo.logo_title)
    print("This challenge includes 10 True/False questions.\n")
    print("Your task is to find the correct answer and type either 'true' or 'false' in terminal.\n")
    print("You may type 'quit' to quit the quiz anytime.\n")



# start_quiz()
# quiz_info()



# Run quiz
quiz = quiz.quiz.Quiz(quiz_question_list)
while not quiz.end_of_quiz():
    quiz.reveal_question()

# Export results to user database
score_list = quiz.score_list
user_database = UserDatabase(345,score_list)
user_database.calculate_final_score()

