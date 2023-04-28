import os

# https://github.com/theskumar/python-dotenv
# take environment variables from .env.
from dotenv import load_dotenv
load_dotenv()

SKILLS_DIR = os.getenv("SKILLS_DIR")

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
        choice_prompt = "Enter the number of the corresponding skill (or 'q' to quit): "
        invalid_choice_prompt = """
Invalid choice. 
Please enter a number between 1 and {} or 'q' to quit.".format(len(self.skills))
"""

        while True:
            choice = input(choice_prompt)
            if choice == 'q':
                return None
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.skills):
                    return self.skills[choice-1]
                else:
                    print(invalid_choice_prompt)
            except ValueError:
                print(invalid_choice_prompt)
