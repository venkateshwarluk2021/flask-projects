import unittest
from quiz_app import Question, Quiz

class TestQuestion(unittest.TestCase):

    def setUp(self):
        self.question_text = "What is the capital of France?"
        self.correct = "Paris"
        self.incorrect = ["London","Berlin","Rome"]
        self.question = Question(self.question_text, self.correct, self.incorrect)


    def test_correct_answer(self):
        correct_index = self.question.options.index(self.correct)
        user_input = chr(65 + correct_index)
        self.assertTrue(self.question.is_correct(user_input))

    def test_incorrect_answer(self):
        for idx, opt in enumerate(self.question.options):
            if opt != self.correct:
                user_input = chr(65+idx)
                self.assertFalse(self.question.is_correct(user_input))

    def test_invalid_input(self):
        self.assertFalse(self.question.is_correct("Z"))
        self.assertFalse(self.question.is_correct(""))

class TestQuiz(unittest.TestCase):

    def test_quiz_initialization(self):
        sample_questions = [
            {
                "question": "2+2?",
                "correct_answer": "4",
                "incorrect_answers": ["2", "3", "5"]
            },
            {
                "question": "3*3?",
                "correct_answer": "9",
                "incorrect_answers": ["6", "3", "12"]
            }
        ]

        quiz = Quiz(sample_questions)
        self.assertEqual(len(quiz.questions), 2)
        self.assertEqual(quiz.score, 0)


if __name__ == "__main__":
    unittest.main()
