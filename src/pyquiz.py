# src/pyquiz.py

import os
import pyfiglet
import markdown
import random

# To use your own settings, set USER_MODE to True
# Then set the USER_SKILLS_DIR and USER_NUM_QUESTIONS values below
USER_MODE = False
USER_SKILLS_DIR = "../pyquiz-skills"
USER_NUM_QUESTIONS = 15

# The default directory containing the example skills quizzes
DEFAULT_SKILLS_DIR = "./skills"

# The default number of questions to ask in a quiz
DEFAULT_NUM_QUESTIONS = 3

# TODO: handle settings
if USER_MODE:
    SKILLS_DIR = USER_SKILLS_DIR
    NUM_QUESTIONS = USER_NUM_QUESTIONS
else:
    SKILLS_DIR = DEFAULT_SKILLS_DIR
    NUM_QUESTIONS = DEFAULT_NUM_QUESTIONS


class Skill:
    """
    A class that represents a skill.

    Parameters:
    skill_name (str): The name of the skill.
    skill_dir (str): The directory where the skill is located.
    """
    def __init__(self, skill_name, skill_dir):
        self.skill_name = skill_name
        self.skill_dir = skill_dir

class SkillsList:
    """
    A class that represents a list of available skills.

    Methods:
    get_available_skills(): Gets the list of available skills.
    display_skills(): Displays the available skills.
    select_skill(): Allows the user to select a skill to quiz on.
    """
    def __init__(self):
        self.skills = self.get_available_skills()

    def get_available_skills(self):
        """
        Gets the list of available skills in the skills directory.

        Returns:
        list: The list of available skills.
        """
        skills = []
        for skill in os.listdir(SKILLS_DIR):
            if os.path.isdir(os.path.join(SKILLS_DIR, skill)):
                skills.append(skill)
        return skills

    def display_skills(self):
        """
        Displays the available skills.
        """
        print("Available skills:")
        for i, skill in enumerate(self.skills, 1):
            print("{}. {}".format(i, skill))
        print()

    def select_skill(self):
        """
        Allows the user to select a skill to quiz on.

        Returns:
        str: The selected skill.
        None: If the user chooses to quit.
        """
        while True:
            choice = input("Enter the number of the skill you want to quiz on (or 'q' to quit): ")
            if choice == 'q':
                return None
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.skills):
                    return self.skills[choice-1]
                else:
                    print("Invalid choice. Please enter a number between 1 and {} or 'q' to quit.".format(len(self.skills)))
            except ValueError:
                print("Invalid choice. Please enter a number or 'q' to quit.")

class QuestionsFile:
    """
    A class that represents a file containing quiz questions.

    Parameters:
    file_path (str): The path to the quiz questions file.

    Methods:
    parse_questions(): Parses the questions from the file.
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

            # Split questions using the "#### Q" pattern
            questions = file_contents.split("#### Q")[1:]
            questions_list = QuestionsList()
            for question in questions:
                # Add question to questions_list
                questions_list.append(Question(question))

            return questions_list

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
        while current_line.startswith('-') == False:
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

                # is this the correct answer?
                if '[x]' in line:
                    correct = True

                # if there is a current choice, add it to the list as it is complete
                if current_choice is not None:

                    self.add_choice(current_choice, correct)
                    correct = False

                # make this the current choice
                current_choice = line.split('] ')[1]

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

        if hasattr(self, 'explanation'):
            print(self.explanation)
            print()
        
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

            print()
            question_ct += 1

            # prompt to hit enter to continue to the next question
            input("Press enter to continue to the next question...")

            # clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')


        print("You scored {}/{}.".format(self.score, len(self.questions)))
        print()

if __name__ == '__main__':
    """
    The main function.
    """

    # welcome
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # welcome message
    print("Welcome to pyquiz!")
    print()

    # ascii art
    pyquiz_art = pyfiglet.figlet_format("pyquiz")
    print(pyquiz_art)
    print()

    # skills
    skills_list = SkillsList()
    skills_list.display_skills()
    selected_skill = skills_list.select_skill()
    if selected_skill:
        print("You selected skill: {}".format(selected_skill))
        print()

    # questions
    questions_path = os.path.join(SKILLS_DIR, selected_skill, "{}-quiz.md".format(selected_skill))
    if os.path.exists(questions_path):
        
        # parse questions
        questions_file = QuestionsFile(questions_path)
        questions_list = questions_file.parse_questions()

        # display example question
        # questions_list.display_example()

        # quiz
        quiz = Quiz(selected_skill, questions_list.get_random_questions())
        quiz.display_quiz()