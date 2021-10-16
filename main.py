from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))


# for item in question_bank:
#     print(item.text)
#     print(item.answer)

qbrain = QuizBrain(question_bank)
while qbrain.still_has_question():
    qbrain.next_question()

print("You've completed the QUIZ...")
print(f"Your final score is: {qbrain.score}/{qbrain.qNo}")