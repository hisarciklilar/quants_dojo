# import gspread
# from google.oauth2.service_account import Credentials

from quiz.assets.question_list import question_list
import quiz.quiz
import quiz.assets.logo as logo

def start_quiz():
    print("Welcome to Quants Dojo!\n\n")
    print("This is a place where you can test your Econometrics skills \n \n")
    print("Ready for the challenge?! \n\n")


quiz = quiz.quiz.Quiz(question_list)
print(logo.logo_title)

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
