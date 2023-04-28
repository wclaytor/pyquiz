import os
import datetime

# https://github.com/theskumar/python-dotenv
# take environment variables from .env.
from dotenv import load_dotenv
load_dotenv()

# results directory
RESULTS_DIR = os.getenv("RESULTS_DIR")

class QuizResults:
    """
    A class that represents a list of results.

    Parameters:
    results (list): A list of Result objects.

    Methods:
    append(): Appends a result to the list.
    display_results(): Displays all results in the list.
    """
    def __init__(self, skill_name, results = []):
        self.skill_name = skill_name
        self.results = results
    
    def __len__(self):
        return len(self.results)

    def append(self, result):
        """
        Appends a result to the list.

        Parameters:
        result (Result): The result to append.
        """
        self.results.append(result)

    def set_score(self, score):
        """
        Sets the score.

        Parameters:
        score (int): The score.
        """
        self.score = score
        # print("Per the results, the score has been set: {}".format(self.score))

    def display_results_summary(self):
        """
        Displays a summary of the results.
        """
        # summary
        print("Quiz Results Summary:")
        print("You scored {}/{}.".format(self.score, len(self.results)))
        print()

    def display_results(self):
        """
        Displays all results in the list.
        """
        # summary
        self.display_results_summary()

        # results
        for result in self.results:
            print ("")
            result.display_result()
            print ("")

    def write_markdown_results(self):
        """
        Writes the results to a markdown file.

        The file is written to the results directory in the following format:
        <skill_name>/<date_time>-quiz-results.md

        The file is written in the following format:
        ## <skill_name>

        ## Quiz Results

        ### <date_time>

        <question_1_markdown>

        <question_2_markdown>

        ...

        @todo: 
        - refactor heading template

        """
        # get the current date and time
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d-%H-%M-%S")

        # create the results directory if it doesn't exist
        if not os.path.exists(RESULTS_DIR):

            # create the results directory
            os.mkdir(RESULTS_DIR)

        # create the skill directory if it doesn't exist
        skill_dir = os.path.join(RESULTS_DIR, self.skill_name)
        if not os.path.exists(skill_dir):
                
            # create the skill directory
            os.mkdir(skill_dir)

        # create the results file
        results_file = os.path.join(skill_dir, "{}-quiz-results.md".format(date_time))

        # output message
        print("Writing results to file: {}".format(results_file))
        print()

        # heading (iqnore ruff for now...)
        heading = """## {}
## Quiz Results
### Summary:
**Date:** {}

**Score:** {}/{}

**Percentage:** {}%

---
### Questions:
""".format(self.skill_name, date_time, self.score, len(self.results), (self.score / len(self.results)) * 100)  # noqa: E501
        
        # write the results to the file
        with open(results_file, "w") as f:
            # write the heading
            f.write(heading)

            for result in self.results:
                f.write(result.get_result_markdown())
                f.write("\n\n---\n\n")

    def write_html_results(self):
        """
        Writes the results to an html file.
        """
        # get the current date and time
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d-%H-%M-%S")

        # create the results directory if it doesn't exist
        if not os.path.exists(RESULTS_DIR):

            # create the results directory
            os.mkdir(RESULTS_DIR)

        # create the skill directory if it doesn't exist
        skill_dir = os.path.join(RESULTS_DIR, self.results[0].question.skill_name)
        if not os.path.exists(skill_dir):
                
                # create the skill directory
                os.mkdir(skill_dir)

        # create the results file
        results_file = os.path.join(skill_dir, "{}-quiz-results.html".format(date_time))

        # write the results to the file
        with open(results_file, "w") as f:
            for result in self.results:
                f.write(result.get_result_html())
                f.write("\n\n")

