class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # continue_game = True
        # while continue_game:
        #     self.next_question()
        #     if self.question_number < len(self.question_list):
        #         continue_game = False
        #         print("You have finished the quiz game!  Thanks for playing")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q.{self.question_number} {current_question.text}. (True or False): ")
        self.check_answer(users_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
        else:
            print("You got it wrong Sorry")
        print(f"Correct answer is {current_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
