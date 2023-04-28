import os
from src.pq.quizResults import QuizResults
from src.pq.result import Result

class Quiz:
    """
    A class that represents a quiz.

    Parameters:
    skill_name (str): The name of the skill.
    questions (QuestionsList): A list of questions.

    Methods:
    display_quiz(): Displays the quiz.
    """

    def __init__(self, skill_name, questions):
        self.skill_name = skill_name
        self.questions = questions
        self.score = 0

    def display_quiz(self):
        """
        Displays the quiz.
        """

        print()
        print("This is a practice quiz for: {}".format(self.skill_name))
        print()

        # prompt to hit enter to continue to start the quiz
        input("Press enter to start the quiz...")

        # clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # create a new QuizResults object
        quiz_results = QuizResults(self.skill_name)

        question_ct = 1
        for question in self.questions:

            # display questions
            question.display_question(question_ct)
            answer = input("Enter your answer: ")

            # check answer
            if question.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")

            quiz_results.append(Result(question, answer))

            print()
            question_ct += 1

            # prompt to hit enter to continue to the next question
            input("Press enter to continue to the next question...")

            # clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')

        # display quiz complete message
        print("Quiz complete!")
        print()
        print("You scored {}/{}.".format(self.score, len(self.questions)))
        print()

        # set the score
        quiz_results.set_score(self.score)

        # display quiz results
        # quiz_results.display_results_summary()

        # write quiz results to file
        quiz_results.write_markdown_results()
