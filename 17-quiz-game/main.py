from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = [Question(q["text"], q["answer"]) for q in question_data]
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print("You've completed the quiz!")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.q_no}.")