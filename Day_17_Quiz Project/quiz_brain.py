class QuizBrain:
    def __init__(self, q_bank) -> None:
        self.question_number = 0
        self.questions_list = q_bank
        self.score = 0
    def next_question(self):
        question_item_text = self.questions_list[self.question_number].text
        question_item_answer = self.questions_list[self.question_number].answer
        while True:
            user_answer = input(f"Q.{self.question_number+1}: {question_item_text} (True/False)?: ").lower()
            if user_answer == "true" or user_answer == "false":
                break
            else:
                print("Invalid response. Please try again.")
        self.check_answer(user_answer, question_item_answer)
        self.question_number += 1
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong! :(")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")