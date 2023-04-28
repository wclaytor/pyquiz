import os
import pyfiglet

from src.pq.skillsList import SkillsList
from src.pq.questionsFile import QuestionsFile
from src.pq.quiz import Quiz

# https://github.com/theskumar/python-dotenv
# take environment variables from .env.
from dotenv import load_dotenv
load_dotenv()

SKILLS_DIR = os.getenv("SKILLS_DIR")

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
        # quiz = Quiz(selected_skill, questions_list.get_first_question())
        # quiz = Quiz(selected_skill, questions_list.get_last_question())

        # create quiz with random questions
        quiz = Quiz(selected_skill, questions_list.get_random_questions())

        # display quiz
        quiz.display_quiz()