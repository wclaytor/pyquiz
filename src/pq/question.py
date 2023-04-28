# question designator
QUESTION_DESIGNATOR = "#### Q"

class Question:
    """
    A class that represents a quiz question.

    Parameters:
    question_text (str): The text of the question.

    Methods:
    parse_question(): Parses the question.
    parse_heading(): Parses the question heading.
    parse_contents(): Parses the question contents.
    parse_choices(): Parses the question choices.

    Attributes:
    question_text (str): The text of the question.
    question_data (list): The question data.
    question_data_line (int): The current line of the question data.
    heading (str): The heading of the question.
    contents (list): The contents of the question.
    choices (list): The choices of the question.
    answer (str): The answer to the question.

    """

    def __init__(self, question_text):
        self.question_text = question_text
        self.question_markdown = QUESTION_DESIGNATOR + question_text
        self.parse_question()
 
    def parse_question(self):
        """
        Parses the question.
        """
        # question_data
        self.question_data = self.question_text.split("\n")
        self.parse_heading()
        self.parse_contents()
        self.parse_choices()

    def parse_heading(self):
        """
        Parses the question heading.
        """
        
        # the first line should be in the format "1. Question heading"
        # but there are questions that have the number but don't have a heading
        dot_splitter = '. '
        heading_array = self.question_data[0].split(dot_splitter)
        if len(heading_array) > 1:
            self.heading = heading_array[1]

        else:
            self.heading = "Untitled Question"

    def parse_contents(self):
        """
        Parses the question contents.
        """

        # contents of question is everything between the heading and the answer choices
        contents = []
        self.question_data_line = 1
        current_line = self.question_data[self.question_data_line]
        while current_line.startswith("-") is False:
            if current_line != '```':
                contents.append(current_line)

            self.question_data_line += 1
            current_line = self.question_data[self.question_data_line]

        self.contents = contents

    def parse_choices(self):
        """
        Parses the question choices.

        TODO: 
        - update to use markdown for parsing choices
        - update to streamline parsing

        """
        self.choices = []
        current_choice = None
        correct = False

        for line in self.question_text.split('\n'):
            # this is the explanation
            if line.startswith('**'):
                break

            # this is a new choice
            if line.startswith('- ['):

                # if there is a current choice, add it to the list as it is complete
                if current_choice is not None:

                    # add choice
                    self.add_choice(current_choice, correct)

                    # reset correct
                    correct = False

                # is this the correct answer?
                # note: this must occur after the previous choice is added to the list
                if '[x]' in line:
                    correct = True

                # make this the current choice
                # this could be a multi-line choice with no text on this line
                current_choice_array = line.split('] ')
                if len(current_choice_array) > 1:
                    current_choice = current_choice_array[1]
                else:
                    current_choice = " \n"

            # this is a continuation of the current choice
            elif current_choice is not None:
                current_choice += '\n' + line

        # add the last choice to the list
        if current_choice is not None:
            
            self.add_choice(current_choice, correct)

    def add_choice(self, choice, correct):
        """
        Adds a choice to the question.

        Parameters:
        choice (str): The choice to add.
        correct (bool): Whether the choice is the correct answer.
        """
        # if the choice ends with a newline, remove it
        if choice.endswith('\n'):
            choice = choice[:-1]

        # add the choice to the list
        self.choices.append(choice)

        # if the choice is correct, set it
        if correct:
            self.correct_answer = len(self.choices)
  
    def parse_explanation(self):
        """
        Parses the question explanation.
        """
        ct = 0
        lines = self.question_text.split('\n')
        for line in lines:
            ct += 1
            # look for a line that startst with "**"
            if line.startswith('**'):
                explanation = line
                break

        # include the rest of the lines
        for line in lines[ct:]:
            explanation += '\n' + line

        self.explanation = explanation

    def display_question(self, question_ct):
        """
        Displays the question.
        
        Parameters:
        question_ct (int): The question number.
        """
        
        # heading
        # the heading should combine the question number and the heading
        print()
        print("{}. {}".format(question_ct, self.heading))
        print()

        # contents
        for line in self.contents:
            print(line)

        print()   

        for i, answer in enumerate(self.choices, 1):
            print("{}. {}".format(i, answer))
        
        print()

        # explanation
        if hasattr(self, 'explanation'):
            print(self.explanation)
            print()

        # display correct answer for debugging
        # print("Correct answer: {}".format(self.correct_answer))
        # print()

    def get_question_markdown(self):
        """
        Returns the question in markdown format.
        """
        return self.question_markdown
    
    def display_question_markdown(self):
        """
        Displays the question in markdown format.
        """
        print(self.question_markdown)
        
    def check_answer(self, answer):
        """
        Checks if the answer is correct.

        Parameters:
        answer (str): The answer to check.

        Returns:
        bool: True if the answer is correct, False otherwise.
        """

        try:
            answer = int(answer)
            if answer == self.correct_answer:
                return True
            else:
                return False
        except ValueError:
            return False

    def get_correct_answer(self):
        """
        Returns the correct answer.
        """
        return self.correct_answer
    