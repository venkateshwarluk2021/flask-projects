import requests
import html
import json

# Step 1: Fetch questions from OpenTDB API
url = "https://opentdb.com/api.php?amount=10&type=multiple"
response = requests.get(url)
data = response.json()

quiz_questions = []

for item in data["results"]:
    question = html.unescape(item["question"])
    correct = html.unescape(item["correct_answer"])
    incorrect = [html.unescape(ans) for ans in item["incorrect_answers"]]

    quiz_questions.append({
        "question":question,
        "correct_answer": correct,
        "incorrect_answers": incorrect
        })

    # Step 3: Save to a Python file
    with open("quiz_data.py", "w" , encoding="utf-8") as fp:
        fp.write("quiz_questions=")
        json.dump(quiz_questions, fp ,indent=4)
