import gspread
from google.oauth2.service_account import Credentials
import datetime
import time
from rich.progress import Progress
from rich.console import Console
from rich.panel import Panel
from quiz.quiz_generator import QUIZ_LENGTH

console = Console()

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
    """
    Initializes attributes and defines methods required to interact with user data spreadsheet
    """

    def __init__(self):
        """
        Initializes UserDatabase attributes
        """
        self.user_id = 0
        self.score_list = []
        self.quiz_score = 0 
        self.previous_score = 0
        self.previous_date_time = None
        self.first_attempt = True
    
    
    def call_user_id_list(self):
        """
        Returns user id list from owner's user database spreadsheet
        """
        user_id_list_str = SHEET.worksheet("user_list").col_values(1)
        user_id_list_str.pop(0)
        user_id_list = [int(id) for id in user_id_list_str]
        return user_id_list

        
    def calculate_final_score(self):
        """
        Wraps user's correct/incorrect responses in a list that is used to calculate quiz score
        """
        quiz_response_sheet = SHEET.worksheet("quiz_response")
        if len(self.score_list) != QUIZ_LENGTH:
            missing_responses = QUIZ_LENGTH - len(self.score_list)
            console.print(f"You did not answer {missing_responses} remaining questions\n\n", style="cyan bold")
            for i in range(missing_responses):
                self.score_list.append(0)
        
        with Progress() as progress:
            task = progress.add_task("[blue bold]Calculating quiz score...", total=3)
            
            self.calculate_quiz_score()
            progress.update(task, advance =1)
            time.sleep(1)

            self.score_list.insert(0, self.user_id)
            self.score_list.append(self.quiz_score)
            self.add_date_to_quiz_record()
            progress.update(task, advance = 1)
            time.sleep(1)

            self.call_previous_score()
            quiz_response_sheet.append_row(self.score_list)
            progress.update(task, advance =1)
            time.sleep(1)        
        
        self.print_score()


    def calculate_quiz_score(self):
        """ 
        Calculates user's quiz score based on a list of responses
        """
        self.quiz_score = (sum(self.score_list) / QUIZ_LENGTH) * 100


    def add_date_to_quiz_record(self):
        """
        Adds date-time stamp to user's score list
        """
        date_time = datetime.datetime.now().strftime("%c")
        self.score_list.append(date_time)


    def call_previous_score(self):
        """
        Checks user's latest previous score and provides feedback on performance
        """
        quiz_score_list_str = SHEET.worksheet("quiz_response").col_values(12)   
        recorded_user_id_list_str = SHEET.worksheet("quiz_response").col_values(1) 
        date_time = SHEET.worksheet("quiz_response").col_values(13)   
        
        quiz_score_list_str.pop(0)
        recorded_user_id_list_str.pop(0)
        date_time.pop(0)
        
        quiz_score_list = [int(score) for score in quiz_score_list_str]
        recorded_user_id_list = [int(id) for id in recorded_user_id_list_str]
        
        if self.user_id == 999:
            self.first_attempt = True
        elif self.user_id in recorded_user_id_list:
            self.first_attempt = False
            recorded_user_id_list.reverse()
            quiz_score_list.reverse()
            date_time.reverse()

            index = recorded_user_id_list.index(self.user_id)
            self.previous_score = quiz_score_list[index]
            self.previous_date_time = date_time[index]

    def print_score(self):
        """
        Prints user's quiz score while calling the latest previous quiz performance for repeating users
        """
        if not self.first_attempt:
            print("\n")
            console.print(" " * 5 + f":white_heavy_check_mark: You scored {self.quiz_score}% on this attempt.\n", style = "violet bold")
            console.print(" " * 5 + f":white_heavy_check_mark: Your previous score was {self.previous_score}% on {self.previous_date_time}\n", style = "violet bold") 
            
            
            self.provide_feedback()
        else:
            print("\n")
            console.print(Panel.fit(" " * 7+f"You scored {self.quiz_score}% on this quiz.\n\n :glowing_star: Come back to increase your test score! :glowing_star:", style = "violet bold", title = "Quiz Results", padding = 1))

    def provide_feedback(self):
        """ 
        Provides feedback based on a comparison of previous and current scores
        """
        if self.quiz_score > self.previous_score:
            console.print(" " * 5 + ":white_heavy_check_mark: Your score has increased in comparison to previous time! Well done on your improvement! :partying_face:", style="violet bold")
        if self.quiz_score == self.previous_score:
            console.print(" " * 5 + ":white_heavy_check_mark: Your score has remained the same in comparison to last time. :neutral_face:", style="violet bold")
        if self.quiz_score < self.previous_score:
            console.print(" " * 5 + ":white_heavy_check_mark: Your score has decreased since last time. :fearful:", style="violet bold")