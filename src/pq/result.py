class Result:
    """
    A class that represents a result.

    Parameters:
    question (Question): The question.
    answer (str): The user provided answer.

    Methods:
    display_result(): Displays the result.

    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.correct_answer = question.get_correct_answer()
        self.result = question.check_answer(answer)

    def display_result(self):
        """
        Displays the result.
        """
        print("Question:")
        print(self.question.question_text)
        print()
        print("Your answer: {}".format(self.answer))
        print()
        print("Correct answer: {}".format(self.correct_answer))
        print()
        print("Result: {}".format(self.result))
        print()

    def get_result(self):
        """
        Returns the result.
        """
        return self.result
    
    def get_result_markdown(self):
        """
        Returns the result in markdown format.
        """
        # question markdown
        output = self.question.question_markdown
        output += "\n\n"

        # answer markdown
        output += "**Your answer:** {}".format(self.answer)
        output += "\n\n"

        # correct answer markdown
        output += "**Correct answer:** {}".format(self.correct_answer)
        output += "\n\n"

        # result markdown
        output += "**Result:** {}".format(self.result)
        output += "\n\n"

        return output
    
    def get_result_html(self):
        """
        Returns the result in html format.
        """
        # ignore ruff line too long
        # pylint: disable=line-too-long
        return "<p><strong>Question:</strong> {}</p><p><strong>Your answer:</strong> {}</p><p><strong>Correct answer:</strong> {}</p><p><strong>Result:</strong> {}</p>".format(self.question.question_text, self.answer, self.correct_answer, self.result) # noqa: E501
    