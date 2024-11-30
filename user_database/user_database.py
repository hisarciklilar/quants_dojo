import gspread
from google.oauth2.service_account import Credentials
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

    def __init__(self, user_id, score_list):
        self.user_id = user_id
        self.score_list = score_list

    def calculate_final_score(self):
        quiz_response_sheet = SHEET.worksheet("quiz_response")
        # data = quiz_response_sheet.get_all_values()
        if len(self.score_list) == QUIZ_LENGTH:
            print("You answered all questions")
        else:
            print("You did not answer all questions")
            missing_responses = QUIZ_LENGTH - len(self.score_list)
        for i in range(missing_responses):
            self.score_list.append(0)
        print(self.score_list)
        final_score = (sum(self.score_list) / QUIZ_LENGTH) * 100
        print(f"Your final score is {final_score}%")
        self.score_list.insert(0, self.user_id)
        self.score_list.append(final_score)
        print(self.score_list)
        quiz_response_sheet.append_row(self.score_list)

