class QuizBrain:
    """Brain of our quizgame for this lesson
    """
    def __init__(self, questions:list):
        """Generate a Quizbrain

        Args:
            questions (list): List of questions you would like to use in the quz show, list contains a dict of question:answer pairings
        """
        self.num = 0
        self.score = 0
        self.question_list = questions
        self.user_answer = ''


    def still_has_quesitons(self):
        """Check if there are questions remaining

        Returns:
            bool: True if num (current question) is not great than the length of the question list
        """
        return self.num < len(self.question_list)


    def get_question(self):
        """Generate a question for the user to answer,
        Check the answer
        """
        current_question = self.question_list[self.num]
        self.user_answer = input(f"Q.{self.num + 1} {current_question.text} True or False?\n>>")
        if self.check_answer(current_question):    
            self.score +=1
        self.num +=1 
        print(f"Your score is {self.score}/{self.num}")
        

    def check_answer(self,question):
        """Check the answer provided by the user

        Args:
            question (Question): the question, and answer dict for the current question

        Returns:
            bool: True if answer is correct, if False ask user to try again
        """
        if question.answer.lower() == self.user_answer.lower():
            return True
        else:
            print("Try again :(")
            return False

    def final_score(self):
        """Thank user for playing and print out their final score
        """
        print("\n\n\t\tThank you for playing!")
        print(f"\t\tYour final score was {self.score}/{self.num}")