# src/pyquiz.py

import os
import pyfiglet

from src.pq.skillsList import SkillsList
from src.pq.questionsFile import QuestionsFile
from src.pq.quiz import Quiz

# To use your own settings, set USER_MODE to True
# Then set the USER_SKILLS_DIR and USER_NUM_QUESTIONS values below
USER_MODE = False
USER_SKILLS_DIR = "../pyquiz-skills"
USER_NUM_QUESTIONS = 5

# The default directory containing the example skills quizzes
DEFAULT_SKILLS_DIR = "./skills"

# The default number of questions to ask in a quiz
DEFAULT_NUM_QUESTIONS = 5

# question designator
QUESTION_DESIGNATOR = "#### Q"

# results directory
RESULTS_DIR = "./results"

# TODO: handle settings
if USER_MODE:
    SKILLS_DIR = USER_SKILLS_DIR
    NUM_QUESTIONS = USER_NUM_QUESTIONS
else:
    SKILLS_DIR = DEFAULT_SKILLS_DIR
    NUM_QUESTIONS = DEFAULT_NUM_QUESTIONS
 
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
    questions_path = os.path.join(SKILLS_DIR, 
                                  selected_skill, 
                                  "{}-quiz.md".format(selected_skill))
    
    if os.path.exists(questions_path):
        
        # parse questions
        questions_file = QuestionsFile(questions_path)
        questions_list = questions_file.parse_questions()

        # display example question
        # questions_list.display_example()

        # create quiz with just the first or last question (helpful for debugging)
        quiz = Quiz(selected_skill, questions_list.get_first_question())
        # quiz = Quiz(selected_skill, questions_list.get_last_question())

        # create quiz with random questions
        # quiz = Quiz(selected_skill, questions_list.get_random_questions())

        # display quiz
        quiz.display_quiz()