import gspread
from google.oauth2.service_account import Credentials
# import os
import quiz.quiz
# import quiz.assets.logo as logo
from quiz.assets.question_bank import question_list
import quiz.quiz_generator
import quiz.quiz_start as quiz_start

QUIZ_LENGTH = 10

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("quants_dojo")


# Generate quiz
quiz_generator = quiz.quiz_generator.QuizGenerator(question_list,QUIZ_LENGTH)
quiz_question_list = quiz_generator.generate_quiz()

# Start quiz
quiz_start.quiz_start()

# Run quiz
quiz = quiz.quiz.Quiz(quiz_question_list)

while not quiz.end_of_quiz():
    quiz.reveal_question()
    
print(f"Here is a summary of your performance {quiz.score_list}")

quiz_response_sheet = SHEET.worksheet("quiz_response")
data = quiz_response_sheet.get_all_values()

# score_list=[1, 1, 0]
if len(quiz.score_list) == len(quiz_question_list):
    print("You answered all questions")
else:
    print("You did not answer all questions")
    missing_responses = len(quiz_question_list) - len(quiz.score_list)
    for i in range(missing_responses):
        quiz.score_list.append(0)
    print(quiz.score_list)

final_score = (sum(quiz.score_list) / QUIZ_LENGTH) * 100
print(f"Your final score is {final_score}%")
user_id =[456]
quiz.score_list.insert(0, user_id[0])
quiz.score_list.append(final_score)
print(quiz.score_list)
quiz_response_sheet.append_row(quiz.score_list)

# quiz_response_sheet.update([score_list], 'B8')
# populated_rows = quiz_response.col_values(1)
# next_row = "B" + str(len(populated_rows) + 1)

