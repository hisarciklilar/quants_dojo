# External libraries
import os
from rich import print
from rich.panel import Panel
from rich.console import Console

console = Console()


class Quiz:
    """
    Initializes attributes and defines methods required to run the quiz
    """

    def __init__(self, question_list):
        """
        Initializes Quiz attributes
        """
        self.question_index = 0
        self.question_list = question_list
        self.response = ""
        self.score = 0
        self.question_progress = True
        self.score_list = []

    def clear_terminal(self):
        """
        Clears console for new question
        """
        print("\n")
        input("Press enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

    def end_of_quiz(self):
        """
        Ends quiz when user completes questions or quits
        """
        q_index = self.question_index
        q_list = self.question_list
        if q_index >= len(q_list) or self.response.lower() == "quit":
            console.print(" " * 20 + "END OF QUIZ!" + "\n",
                          style="yellow bold")
            return True

    def reveal_question(self):
        """
        Prints next question on screen and
        passes user's input to check_answer()
        """
        while self.question_progress:
            self.clear_terminal()
            q_index = self.question_index
            q_list = self.question_list
            question_to_reveal = q_list[q_index]["question"]
            print(f"\nQ.{self.question_index + 1}: True or False?\n\n")
            self.response = input(f"'{question_to_reveal}' (True/False)\n")
            self.check_answer()

        self.question_progress = True
        self.question_index += 1

    def check_answer(self):
        """
        Provides feedback on user's input to question
        """
        valid_answers = ["true", "false"]
        correct_answer = self.question_list[self.question_index]["answer"]

        if self.response.strip().lower() == correct_answer.lower():
            self.score += 1
            console.print("\n\nCorrect! :party_popper: \n\n",
                          style="magenta bold")
            console.print(f"The answer was [bold]{correct_answer}[/bold]\n\n")
            scr = self.score
            tot = self.question_index + 1
            score = round((self.score / (self.question_index + 1))*100, 2)
            txt_1 = "You have answered "
            txt_2 = "Your current score is "
            print(Panel.fit(txt_1 + f"{scr} of {tot} questions correctly\n" +
                            "\n" * 2 + " " * 8 + txt_2 + f"{score}%",
                            style="blue bold", padding=2))
            self.track_score(1)
            self.question_progress = False

        elif self.response.strip().lower() == "quit":
            console.print("\nYou chose to quit the session.\n",
                          style="yellow bold")
            console.print("Hope you come back soon!\n", style="yellow bold")
            self.question_progress = False

        elif self.response.strip().lower() not in valid_answers:
            print("You need to type 'true' or 'false'. Please try again.\n")

        else:
            console.print("\n\nIncorrect. :cross_mark:\n\n",
                          style="magenta bold")
            print(f"The answer was [bold]{correct_answer}[/bold]\n\n")
            scr = self.score
            tot = self.question_index + 1
            score = round((self.score / (self.question_index + 1))*100, 2)
            txt_1 = "You have answered "
            txt_2 = "Your current score is "
            print(Panel.fit(txt_1 + f"{scr} of {tot} questions correctly\n" +
                            "\n" * 2 + " " * 8 + txt_2 + f"{score}%",
                            style="blue bold", padding=2))
            self.track_score(0)
            self.question_progress = False

    def track_score(self, scr):
        """
        Tracks question scores
        """
        self.score_list.append(scr)
