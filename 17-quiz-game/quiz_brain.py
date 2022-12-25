class QuizBrain:
    def __init__(self, question_list):
        self.q_no = 0
        self.q_list = question_list
        self.score = 0

    def next_question(self):
        q = self.q_list[self.q_no]
        self.q_no += 1
        tf_str = "True or False:"
        usr_answer = input(f"Q{self.q_no}. {tf_str} {q.text} ").lower()
        self.check_answer(usr_answer, q.answer)

    def still_has_questions(self):
        return self.q_no < len(self.q_list)

    def check_answer(self, usr_answer, correct_answer):
        if usr_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong. The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.q_no}.")
        print("\n")
