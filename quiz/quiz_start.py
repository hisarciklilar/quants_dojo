# External library
from rich import print
from rich.console import Console
from rich.panel import Panel
# User-written
import quiz.assets.logo as logo
from user_database.user_database import UserDatabase


console = Console()

user = UserDatabase()


def validate_user_id(id):
    """
    Validates user's 'user id' input through checks on the
    length, type, and presence in the user register list.
    """
    valid_user_id_list = user.call_user_id_list()
    try:
        user_id = int(id)
        if len(id) != 3:
            raise ValueError(f"User id does not exist")
        if user_id not in valid_user_id_list:
            raise ValueError(f"User id not found in list of users")
    except ValueError as e:
        console.print(f"Invalid data: {e}, user id must be 3-digit number.\n",
                      style="cyan bold")
        console.print("If you do not have a registered user id, use 999\n",
                      style="cyan bold")
        print("Your progress will not be recorded in that instance\n")
        return False
    return True


def start_quiz():
    """
    Asks for 'user id' in a welcome screen.
    """
    print(logo.logo_picture)
    console.print(Panel.fit(" "* 5 +"""  Welcome to Quants Dojo!
                            \nDare to test your Econometrics skills?""",
                            padding=1, style="blue bold"))
    while True:
        user_id_str = input("Type your USER ID to continue quiz\n").strip()
        if validate_user_id(user_id_str):
            console.print("User id recorded. Starting the quiz...",
                          style="yellow")
            return user_id_str


def quiz_info():
    """
    Display quiz information
    """
    console.print(logo.logo_title, style="magenta bold")
    text = """\
    This challenge includes [blue bold]10[/blue bold] True/False questions.\n
    Your task is to find whether the statement is 'true' or 'false'.\n
    Type:\n
       '[green bold]true[/green bold]' if you think the statement is true.\n
       '[red bold]false[/red bold]' if you think the statement is false.\n
       '[yellow bold]quit[/yellow bold]' if you want to quit the quiz.
    """
    console.print(Panel.fit(text))


def quiz_start():
    """
    Returns 'user id' input by running quiz start and info functions
    """
    user_id_str = start_quiz()
    quiz_info()
    return user_id_str
