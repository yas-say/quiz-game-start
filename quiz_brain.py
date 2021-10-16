class QuizBrain:
    def __init__(self, question_list):
        self.qlist = question_list
        self.qNo = 0
        self.score = 0

    def next_question(self):
        curr_question = self.qlist[self.qNo]
        self.qNo += 1
        user_answer = input(f"Q.{self.qNo}: {curr_question.text} (True/False)?: ")
        self.check_answer(user_answer,curr_question.answer)


    def still_has_question(self):
        if self.qNo <= len(self.qlist) - 1:
            return True
        else:
            return False

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your score is:{self.score}/{self.qNo}")
        print("\n")
