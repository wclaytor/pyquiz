import random

# Number of questions to be asked in a quiz.
NUM_QUESTIONS = 1

class QuestionsList:
    """
    A class that represents a list of questions.

    Parameters:
    questions (list): A list of Question objects.

    Methods:
    append(): Appends a question to the list.
    display_questions(): Displays all questions in the list.
    display_example(): Displays an example question.
    get_random_questions(): Returns a random sample of questions.
    get_first_question(): Returns the first question in the list.
    get_last_question(): Returns the last question in the list.

    Attributes:
    questions (list): A list of Question objects.

    TODO:
    - handle NUM_QUESTIONS
    """

    def __init__(self, questions = []):
        self.questions = questions
    
    def __len__(self):
        return len(self.questions)

    def append(self, question):
        """
        Appends a question to the list.

        Parameters:
        question (Question): The question to append.
        """
        self.questions.append(question)

    def display_questions(self):
        """
        Displays all questions in the list.
        """
        for question in self.questions:
            print ("")
            print (question.display_question())
            print ("")

    def display_example(self):
        """
        Displays an example question.
        """
        question = self.questions[2]
        question.display_question(1)
        print("Correct answer: {}".format(question.correct_answer))
        print()
        
    def get_random_questions(self, num_questions=NUM_QUESTIONS):
        """
        Returns a random sample of questions.

        Parameters:
        num_questions (int): The number of questions to return.

        Returns:
        list: A list of Question objects.
        """
        return random.sample(self.questions, num_questions)

    def get_first_question(self):
        """
        Returns the first question in the list.

        Returns:
        Question: The first question in the list.
        """
        return [self.questions[0]]

    def get_last_question(self):
        """
        Returns the last question in the list.

        Returns:
        Question: The last question in the list.
        """
        return [self.questions[-1]]
