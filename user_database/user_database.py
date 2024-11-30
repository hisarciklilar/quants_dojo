import gspread
from google.oauth2.service_account import Credentials
import datetime
# from run import QUIZ_LENGTH
QUIZ_LENGTH =10 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("quants_dojo")


class UserDatabase:

    def __init__(self):
        self.user_id = 0
        self.score_list = []
        self.quiz_score = 0 
        self.previous_score = 0
    
    
    def call_user_id_list(self):
        user_id_list_str = SHEET.worksheet("user_list").col_values(1)
        user_id_list_str.pop(0)
        user_id_list = [int(id) for id in user_id_list_str]
        return user_id_list

        
    def calculate_final_score(self):
        quiz_response_sheet = SHEET.worksheet("quiz_response")
        if len(self.score_list) == QUIZ_LENGTH:
            print("You answered all questions")
        else:
            print("You did not answer all questions")
            missing_responses = QUIZ_LENGTH - len(self.score_list)
        for i in range(missing_responses):
            self.score_list.append(0)
        print(self.score_list)
        calculate_quiz_score(self)
        self.score_list.insert(0, self.user_id)
        self.score_list.append(self.quiz_score)
        add_date_to_quiz_record(self)
        print(self.score_list)
        call_previous_score(self)
        quiz_response_sheet.append_row(self.score_list)

def calculate_quiz_score(self):
    self.quiz_score = (sum(self.score_list) / QUIZ_LENGTH) * 100

def add_date_to_quiz_record(self):
    date_time = datetime.datetime.now().strftime("%c")
    self.score_list.append(date_time)

def call_previous_score(self):
    quiz_score_list_str = SHEET.worksheet("quiz_response").col_values(12)   
    recorded_user_id_list_str = SHEET.worksheet("quiz_response").col_values(1) 
    quiz_score_list_str.pop(0)
    recorded_user_id_list_str.pop(0)
    quiz_score_list = [int(score) for score in quiz_score_list_str]
    recorded_user_id_list = [int(id) for id in recorded_user_id_list_str]
    print(quiz_score_list)
    print(recorded_user_id_list)
    if self.user_id in recorded_user_id_list:
        print("you took this quiz before")
        recorded_user_id_list.reverse()
        quiz_score_list.reverse()
        index = recorded_user_id_list.index(self.user_id)
        print(index)
        self.previous_score = quiz_score_list[index]
        print(f"Your previous score on this test was {self.previous_score}")
    else:
        print("It is your first attempt.")
