# import gspread
# from google.oauth2.service_account import Credentials
# import os
import quiz.quiz
# import quiz.assets.logo as logo
from quiz.assets.question_bank import question_list
import quiz.quiz_generator
import quiz.quiz_start
from user_database.user_database import UserDatabase
from quiz.quiz_generator import QUIZ_LENGTH

# Generate quiz
quiz_generator = quiz.quiz_generator.QuizGenerator(question_list,QUIZ_LENGTH)
quiz_question_list = quiz_generator.generate_quiz()

# Start quiz
user = UserDatabase()
user_id_str = quiz.quiz_start.quiz_start()
user.user_id = int(user_id_str)

# Run quiz
quiz = quiz.quiz.Quiz(quiz_question_list)
while not quiz.end_of_quiz():
    quiz.reveal_question()

# Export results to user database
#score_list = quiz.score_list

user.score_list = quiz.score_list
user.calculate_final_score()
