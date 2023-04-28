from src.pq.questionsList import QuestionsList
from src.pq.question import Question

# question designator
QUESTION_DESIGNATOR = "#### Q"

class QuestionsFile:
    """
    A class that represents a file containing quiz questions.

    Parameters:
    file_path (str): The path to the quiz questions file.

    Methods:
    parse_questions(): Parses the questions from the file.

    Attributes:
    file_path (str): The path to the quiz questions file.

    TODO: 
    - handle question designator
    
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_questions(self):
        """
        Parses the questions from the file.

        Returns:
        QuestionsList: The list of parsed questions.
        """
        # TODO: update to use markdown for parsing questions
        with open(self.file_path, 'r') as file:
            file_contents = file.read()

            # Split questions using the QUESTION_DESIGNATOR pattern
            questions = file_contents.split(QUESTION_DESIGNATOR)[1:]
            questions_list = QuestionsList()
            for question in questions:
                # Add question to questions_list
                questions_list.append(Question(question))

            return questions_list
