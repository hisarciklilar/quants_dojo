# import gspread
# from google.oauth2.service_account import Credentials

from question_list import question_list

for i in range(len(question_list)):
    print(question_list[i])

for i in range(len(question_list)):
    print(question_list[i]["question"])


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
