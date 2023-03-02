import json

with open('questions.json', 'r') as file_1:
    content = file_1.read()

data = json.loads(content)


for question in data:
    print(question["Question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    user_choice = int(input('Enter your anser: '))
    question["user_choice"] = user_choice

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["Correct_answer"]:
        score = score+1
        result = "Correct Answer"
    else:
        result = "Wrong answer"
    message = f" {index+1} {result} - Your answer: {question['user_choice']}, the correct answer is: {question['Correct_answer']}"
    print(message)


print(score, "/", len(data))
