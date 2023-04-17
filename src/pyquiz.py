import os
import pyfiglet
import markdown
import random

# testing an important update!!!

# The directory containing the skills quizzes
SKILLS_DIR = "./skills"

# The default number of questions to ask in a quiz
DEFAULT_NUM_QUESTIONS = 3

class Skill:
    def __init__(self, skill_name, skill_dir):
        self.skill_name = skill_name
        self.skill_dir = skill_dir

class SkillsList:
    def __init__(self):
        self.skills = self.get_available_skills()

    def get_available_skills(self):
        skills = []
        for skill in os.listdir(SKILLS_DIR):
            if os.path.isdir(os.path.join(SKILLS_DIR, skill)):
                skills.append(skill)
        return skills

    def display_skills(self):
        print("Available skills:")
        for i, skill in enumerate(self.skills, 1):
            print("{}. {}".format(i, skill))
        print()

    def select_skill(self):
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
    def __init__(self, file_path):
        self.file_path = file_path
    # TODO: update to use markdown for parsing questions
    # TODO: update to handle separating questions here, but let the Question class handle the answer choices
    def parse_questions(self):
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

    def __init__(self, question_text):
        self.question_text = question_text

        # question_data
        question_data = question_text.split("\n")

        # heading
        self.heading = question_data[0].split(". ")[1]

        # contents of question is everything between the heading and the answer choices
        contents = []
        question_data_line = 1
        current_line = question_data[question_data_line]
        while current_line.startswith('-') == False:
            if current_line != '```':
                contents.append(current_line)

            question_data_line += 1
            current_line = question_data[question_data_line]

        self.contents = contents

        # Extract answer choices
        choices = []
        current_line = question_data[question_data_line]

        # handle each choice
        while current_line.startswith('-'):

            # choice_text starts after the closing bracket
            choice_text = current_line.split('] ')[1]

            # add choice to choices
            choices.append(choice_text)

            # is this the correct answer?
            if '[x]' in current_line:

                #  this is the correct answer
                self.correct_answer = len(choices)

            question_data_line += 1
            current_line = question_data[question_data_line]

        self.choices = choices

    def display_question(self, question_ct):
        
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
        
    def check_answer(self, answer):
        try:
            answer = int(answer)
            if answer == self.correct_answer:
                return True
            else:
                return False
        except ValueError:
            return False

class QuestionsList:
    def __init__(self, questions = []):
        self.questions = questions

    def append(self, question):
        self.questions.append(question)

    def display_questions(self):
        for question in self.questions:
            print ("")
            print (question.display_question())
            print ("")

    def display_example(self):
        question = self.questions[2]
        question.display_question()
        print("Correct answer: {}".format(question.correct_answer))
        print()
        
    def get_random_questions(self, num_questions=DEFAULT_NUM_QUESTIONS):
        return random.sample(self.questions, num_questions)

class Quiz:
    def __init__(self, skill_name, questions):
        self.skill_name = skill_name
        self.questions = questions
        self.score = 0

    def display_quiz(self):

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


