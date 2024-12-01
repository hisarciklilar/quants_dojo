import os
import quiz.assets.logo as logo
from user_database.user_database import UserDatabase
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
#from rich.panel import Panel

console = Console()

user = UserDatabase()

def validate_user_id(id):
    """
    Validates user's 'user id' input through checks on the length, type and presence in the user register list.
    """
    valid_user_id_list = user.call_user_id_list()
    try: 
        user_id = int(id)
        if len(id) != 3:
            raise ValueError(f"User id does not exist")
        if user_id not in valid_user_id_list:
            raise ValueError(f"User id not found in list of users \n [cyan bold]If you do not have a registered user id, use 999[/cyan bold]\n Your progress will not be recorded in this instance")      
    except ValueError as e:
        print(f"Invalid data: {e}, [cyan bold]your user id should be a number with 3 digits[/cyan bold], please try again.\n")
        return False
    return True


def start_quiz():
    """
    Asks for 'user id' in a welcome screen.
    """
    console.print(logo.logo_picture, style = "magenta bold")
    console.print(Panel.fit(" " * 5 + ":dragon: Welcome to Quants Dojo! :dragon:\n \nReady to test your Econometrics skills?", padding = 1, style = "blue bold"))
    while True:
        # print("\n")
        user_id_str = input("Type your USER ID below and continue to the quiz if you dare!\n").strip()
        if validate_user_id(user_id_str):
            console.print("User id recorded. Starting the quiz...", style = "yellow")
            return user_id_str
            

def quiz_info():
    """
    Display quiz information
    """
    console.print(logo.logo_title, style = "magenta bold")
    console.print(Panel.fit("""This challenge includes [blue bold]10[/blue bold] True/False questions.\n
    Your task is to find whether the statement provided is 'true' or 'false'.\n
    Type: '[green bold]true[/green bold]' if you think the statement is true.\n
    Type: '[red bold]false[/red bold]' if you think the statement is false.\n
    Type: '[yellow bold]quit[/yellow bold]' if you want to quit the quiz half-way through.""", padding = 1))


def quiz_start():
    """
    Returns 'user id' input by running quiz start and info functions
    """
    user_id_str = start_quiz()
    quiz_info()
    return user_id_str
    