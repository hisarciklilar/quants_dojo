import random 


class QuizGenerator:
    def __init__(self, question_data, quiz_length):
        self.quiz_questions = []
        self.question_data = question_data
        self.quiz_length = quiz_length

    def generate_quiz(self):
        for i in range(self.quiz_length):
            question_version = random.randint(0,1)
            print(f"random number generated {question_version}")
            if question_version == 0:
                question_text = self.question_data[i]["question_0"]
                answer_text = self.question_data[i]["answer_0"]
            else:
                question_text = self.question_data[i]["question_1"]
                answer_text = self.question_data[i]["answer_1"]
            self.quiz_questions.append({"question" : question_text, "answer" : answer_text})
            print(self.quiz_questions)
        print(f"Final question list: {self.quiz_questions}")


