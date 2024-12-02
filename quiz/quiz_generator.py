# External library
import random

QUIZ_LENGTH = 10


class QuizGenerator:
    """
    Initializes attributes and defines methods required to generate
    a quiz of desired length from a question bank
    """

    def __init__(self, question_data, quiz_length):
        """
        Initializes QuizGenerator attributes
        """
        self.quiz_questions = []
        self.question_data = question_data
        self.quiz_length = quiz_length

    def generate_quiz(self):
        """
        Generates quiz based on a random draw of
        two versions of the same question
        """
        for i in range(self.quiz_length):
            question_version = random.randint(0, 1)
            if question_version == 0:
                q_text = self.question_data[i]["question_0"]
                a_text = self.question_data[i]["answer_0"]
            else:
                q_text = self.question_data[i]["question_1"]
                a_text = self.question_data[i]["answer_1"]
            self.quiz_questions.append({"question": q_text, "answer": a_text})
        return self.quiz_questions
