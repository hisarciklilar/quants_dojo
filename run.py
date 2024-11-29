# import gspread
# from google.oauth2.service_account import Credentials

import quiz.quiz
import quiz.assets.logo as logo
from quiz.assets.question_bank import question_list as question_list
import quiz.quiz_generator


def start_quiz():
    print("Welcome to Quants Dojo!\n\n")
    print("This is a place where you can test your Econometrics skills \n \n")
    print("Ready for the challenge?! \n\n")


print(logo.logo_title)
print(logo.logo_picture)

quiz_generator = quiz.quiz_generator.QuizGenerator(question_list,3)
quiz_question_list = quiz_generator.generate_quiz()

quiz = quiz.quiz.Quiz(quiz_question_list)

start_quiz()
while not quiz.end_of_quiz():
    quiz.reveal_question()
    

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file("creds.json")
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open("quants_dojo")

# quiz_response = SHEET.worksheet("quiz_response")
# data = quiz_response.get_all_values()

# print(data)
# user_list = SHEET.worksheet("user_list")
# print(user_list.get_all_values())
