import random 


class QuizGenerator:
    def __init__(self, question_data, quiz_length):
        self.quiz_questions = []
        self.question_data = question_data
        self.quiz_length = quiz_length


    def generate_quiz(self):
        """
        Generates quiz based on a random draw of two versions of the same question
        """
        for i in range(self.quiz_length):
            question_version = random.randint(0,1)
            if question_version == 0:
                question_text = self.question_data[i]["question_0"]
                answer_text = self.question_data[i]["answer_0"]
            else:
                question_text = self.question_data[i]["question_1"]
                answer_text = self.question_data[i]["answer_1"]
            self.quiz_questions.append({"question" : question_text, "answer" : answer_text})
        return self.quiz_questions

