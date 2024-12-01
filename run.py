from quiz.quiz import Quiz
from quiz.assets.question_bank import question_list
from quiz.quiz_generator import QuizGenerator
from quiz.quiz_start import quiz_start
from user_database.user_database import UserDatabase
from quiz.quiz_generator import QUIZ_LENGTH
from rich.panel import Panel
from rich.console import Console

console = Console()

def quants_dojo():
    # Generate quiz
    quiz_generator = QuizGenerator(question_list,QUIZ_LENGTH)
    quiz_question_list = quiz_generator.generate_quiz()

    # Start quiz
    user = UserDatabase()
    user_id_str = quiz_start()
    user.user_id = int(user_id_str)

    # Run quiz
    quiz = Quiz(quiz_question_list)
    while not quiz.end_of_quiz():
        quiz.reveal_question()

    # Export results 
    user.score_list = quiz.score_list

    # Calculate score
    user.calculate_final_score()

    restart_quiz()

def restart_quiz():
    print("\n")
    console.print(Panel.fit("Would you like another go? Press enter \n\n Would you like to exit? Type exit", style = "blue bold", title = "Restart the quiz?", padding=1))
    user_choice = input("Your choice?")
    if user_choice == "":
        quants_dojo()
    elif user_choice.strip().lower() == "exit":
        exit()
    else:
        print("Please press enter to play again or type exit to exit")
    
quants_dojo()
