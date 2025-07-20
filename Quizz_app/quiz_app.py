from quiz_data import quiz_questions
import random

class Question:
    def __init__(self, question_text, correct_answer, incorrect_answers):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.options = incorrect_answers+[correct_answer]
        random.shuffle(self.options)

    def display(self):
        print(f"\n{self.question_text}")
        for idx, option in enumerate(self.options):
            print(f"{chr(65+idx)}, {option}")

    def is_correct(self, user_choice):
        if not user_choice or len(user_choice) != 1:
            return False
        try:
            index = ord(user_choice.upper()) - 65
            return self.options[index] == self.correct_answer
        except (IndexError, ValueError):
            return False

class Quiz:

    def __init__(self, questions_data):
        self.questions = [Question(q["question"],q["correct_answer"], q["incorrect_answers"]) for q in questions_data]
        self.score = 0
        self.current_index = 0

    def run(self):
        print("Welcome to the Quiz!\n")
        total = len(self.questions)
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i} of {total} ({total - i} remaining)")
            question.display()
            user_input = input("Your answer (A/B/C/D): ").strip()
            if question.is_correct(user_input):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! Correct answer: {question.correct_answer}\n")
            self.current_index += 1
            print(f"current_score: {self.score}/{i}\n")
        print(f"\n Quiz finished! Your score: {self.score}/{total}")

if __name__ == "__main__":
    quiz = Quiz(quiz_questions)
    quiz.run()
