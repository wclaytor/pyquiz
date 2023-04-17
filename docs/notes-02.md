# py-quiz notes

## 01
Plan
Create a Skill class that represents a skill in which the user can be quizzed. The Skill class should have properties such as skill name, skill directory path, and a method to retrieve the list of available skills from the ./skills directory.

Create a QuestionsFile class that represents a markdown file containing the list of questions for a specified skill. The QuestionsFile class should have properties such as file path, skill name, and a method to parse the markdown file and extract the questions into a list of Question objects.

Create a Question class that represents a single question. The Question class should have properties such as question text, answer choices, and correct answer.

Create a QuestionsList class that represents the list of questions extracted from the QuestionsFile for a specified Skill. The QuestionsList class should have methods to randomly choose 5 questions from the list and to record the user's answers for each question.

Create a Quiz class that represents a quiz for a specified Skill. The Quiz class should use the Skill, QuestionsFile, and QuestionsList classes to create a quiz for the user. The Quiz class should have methods to display the quiz to the user, record the user's answers, calculate the result, and display the result at the end of the quiz.

Implement the user stories, including the ability to choose a skill, take a quiz, review results, practice a quiz, and get a skill badge.

Test the pyquiz script with various skills and different scenarios to ensure it is working correctly and providing accurate results.

Add error handling and input validation to handle any possible errors or invalid inputs from the user.

Create a user-friendly command-line interface (CLI) for the pyquiz script, with clear instructions and prompts for the user.

Add additional features or improvements to enhance the functionality and usability of the pyquiz script, such as allowing the user to customize the number of questions in a quiz, displaying a progress bar during the quiz, and providing hints or explanations for incorrect answers.

Document the usage and functionality of the pyquiz script in a README file, including installation instructions, usage examples, and any other relevant information for users to use the script effectively.

## 02
Create the pyquiz script based on the plan above

-

Sure! Here's an example implementation of the pyquiz script based on the plan outlined above:

```
import os
import random
import markdown

class Skill:
    def __init__(self, skill_name, skill_dir):
        self.skill_name = skill_name
        self.skill_dir = skill_dir

    def get_available_skills(self):
        skills = []
        for skill in os.listdir(self.skill_dir):
            if os.path.isdir(os.path.join(self.skill_dir, skill)):
                skills.append(skill)
        return skills

class QuestionsFile:
    def __init__(self, file_path, skill_name):
        self.file_path = file_path
        self.skill_name = skill_name

    def parse_questions(self):
        questions = []
        with open(self.file_path, 'r') as f:
            md_content = f.read()
            md_questions = markdown.markdown(md_content).split('\n')
            for q in md_questions:
                if 'X' in q:
                    question_text, answer_choices = q.split('X')
                    question_text = question_text.strip()
                    answer_choices = [choice.strip() for choice in answer_choices.split(',')]
                    question = Question(question_text, answer_choices)
                    questions.append(question)
        return questions

class Question:
    def __init__(self, question_text, answer_choices):
        self.question_text = question_text
        self.answer_choices = answer_choices

class QuestionsList:
    def __init__(self, skill_name, questions):
        self.skill_name = skill_name
        self.questions = questions

    def get_random_questions(self, num_questions=5):
        return random.sample(self.questions, num_questions)

class Quiz:
    def __init__(self, skill_name, questions_list):
        self.skill_name = skill_name
        self.questions_list = questions_list
        self.user_answers = {}

    def display_quiz(self):
        print("Welcome to the {} quiz!\n".format(self.skill_name))
        for i, question in enumerate(self.questions_list, 1):
            print("Question {}: {}".format(i, question.question_text))
            print("Answer Choices: {}".format(', '.join(question.answer_choices)))

    def record_user_answer(self, question_num, user_answer):
        self.user_answers[question_num] = user_answer

    def calculate_result(self):
        correct_answers = 0
        total_questions = len(self.questions_list)
        for i, question in enumerate(self.questions_list, 1):
            if i in self.user_answers and self.user_answers[i] in question.answer_choices:
                correct_answers += 1
        result_percentage = (correct_answers / total_questions) * 100
        return result_percentage

    def display_result(self):
        result_percentage = self.calculate_result()
        print("\nQuiz Result for {}: {:.2f}%".format(self.skill_name, result_percentage))
        if result_percentage >= 75:
            print("Pass")
        else:
            print("Fail")

# Main function to run the pyquiz script
def pyquiz():
    skills_dir = './skills'
    print("Welcome to PyQuiz!")
    print("Available Skills: ")
    skill = Skill('', skills_dir)
    available_skills = skill.get_available_skills()
    for i, skill_name in enumerate(available_skills, 1):
        print("{}. {}".format(i, skill_name))
    skill_choice = input("Enter the number of the skill you want to quiz: ")
    if skill_choice.isdigit() and int(skill_choice) in range(1, len(available_skills) + 1):
        skill_name = available_skills[int(skill_choice) - 1]
        skill_dir = os.path.join(skills_dir, skill_name)
        questions_file = os.path.join(skill_dir, "{}-quiz.md".

```

-

The end seems to be cut off. Regenerate starting from # Main function to run the pyquiz script

-

Sure! Here's the continuation of the pyquiz() function:

```
def pyquiz():
    skills_dir = './skills'
    print("Welcome to PyQuiz!")
    print("Available Skills: ")
    skill = Skill('', skills_dir)
    available_skills = skill.get_available_skills()
    for i, skill_name in enumerate(available_skills, 1):
        print("{}. {}".format(i, skill_name))
    skill_choice = input("Enter the number of the skill you want to quiz: ")
    if skill_choice.isdigit() and int(skill_choice) in range(1, len(available_skills) + 1):
        skill_name = available_skills[int(skill_choice) - 1]
        skill_dir = os.path.join(skills_dir, skill_name)
        questions_file = os.path.join(skill_dir, "{}-quiz.md".format(skill_name))
        if os.path.exists(questions_file):
            questions_file = QuestionsFile(questions_file, skill_name)
            questions = questions_file.parse_questions()
            questions_list = QuestionsList(skill_name, questions)
            quiz = Quiz(skill_name, questions_list.get_random_questions())
            quiz.display_quiz()
            for i, question in enumerate(quiz.questions_list, 1):
                user_answer = input("\nAnswer for Question {}: ".format(i))
                quiz.record_user_answer(i, user_answer)
            quiz.display_result()
        else:
            print("Error: Questions file not found for the selected skill.")
    else:
        print("Invalid choice. Please choose a valid skill number.")

# Run the pyquiz script
if __name__ == "__main__":
    pyquiz()

```

This implementation defines the main pyquiz() function that interacts with the user and coordinates the quiz. It prompts the user to select a skill, loads the questions from the corresponding skill directory and displays them, records user answers, calculates the quiz result, and finally displays the result. The quiz uses the Skill, QuestionsFile, Question, QuestionsList, and Quiz classes to manage the different components of the quiz. Note that the implementation assumes that the questions are stored in Markdown format in a file named "{skill_name}-quiz.md" in the corresponding skill directory, as per the initial plan.

## 03
The skills choice seems to work but the questions are not displayed. I get the following error:
```
bpc@pro-15 pyquiz % pipenv run python ./lib/pyquiz.py
Welcome to PyQuiz!
Available Skills: 
1. python
2. ruby-on-rails
3. javascript
Enter the number of the skill you want to quiz: 1
Traceback (most recent call last):
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 112, in <module>
    pyquiz()
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 99, in pyquiz
    quiz = Quiz(skill_name, questions_list.get_random_questions())
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 47, in get_random_questions
    return random.sample(self.questions, num_questions)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/random.py", line 456, in sample
    raise ValueError("Sample larger than population or is negative")
ValueError: Sample larger than population or is negative
bpc@pro-15 pyquiz % 
```

-

Apologies for the error. It looks like there is an issue with the get_random_questions() method in the QuestionsList class, which is causing the "ValueError: Sample larger than population or is negative" error. This error occurs when the number of requested random questions is larger than the total number of questions available in the questions list.

To fix this issue, we can add a check to ensure that the number of requested random questions is not greater than the total number of questions available. Here's an updated version of the get_random_questions() method:

```
class QuestionsList:
    # ...

    def get_random_questions(self, num_questions=5):
        """
        Get a list of random questions from the questions list.

        Args:
            num_questions (int): Number of random questions to get. Defaults to 5.

        Returns:
            list: List of random questions.
        """
        if num_questions > len(self.questions):
            num_questions = len(self.questions)
        return random.sample(self.questions, num_questions)

```

With this update, the code should now handle the case where the number of requested random questions is larger than the total number of questions available, and it should not raise the "ValueError" anymore. Please give it a try and let me know if you encounter any further issues.

## 04
Now I get the following:
```
bpc@pro-15 pyquiz % pipenv run python ./lib/pyquiz.py
Welcome to PyQuiz!
Available Skills: 
1. python
2. ruby-on-rails
3. javascript
Enter the number of the skill you want to quiz: 1
Welcome to the python quiz!

Traceback (most recent call last):
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 123, in <module>
    pyquiz()
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 115, in pyquiz
    quiz.display_result()
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 85, in display_result
    result_percentage = self.calculate_result()
                        ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 81, in calculate_result
    result_percentage = (correct_answers / total_questions) * 100
                         ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
ZeroDivisionError: division by zero
bpc@pro-15 pyquiz % 
```

Note that the sample question files each have 11 questions. The actual files should have over 100 questions.

## 05
You are off track. The issue seems to be that the list of questions is not being parsed correctly so the script thinks there are 0 questions. Fix that error.

-

I apologize for the confusion. Upon reviewing the code again, I realized that the issue is related to the questions_list object not being properly created from the loaded question files. We need to update the get_random_questions() method to correctly parse the questions from the loaded question files.

Here's an updated version of the get_random_questions() method that should resolve the issue:


```
class Question:
    # ...

    @staticmethod
    def parse_question_string(question_string):
        """
        Parse a question string into a Question object.

        Args:
            question_string (str): Question string to parse.

        Returns:
            Question: Parsed Question object.
        """
        # Split the question string into question and answers
        question, *answers = question_string.strip().split("\n")
        # Extract the correct answer from the answers list
        correct_answer = next(answer for answer in answers if answer.startswith("*"))
        # Remove the "*" from the correct answer
        correct_answer = correct_answer[1:].strip()
        # Remove the "*" from the answers list
        answers = [answer[1:].strip() if answer.startswith("*") else answer.strip() for answer in answers]
        return Question(question, answers, correct_answer)

class QuestionsList:
    # ...

    def load_questions_from_file(self, file_path):
        """
        Load questions from a file.

        Args:
            file_path (str): File path.

        Returns:
            list: List of parsed Question objects.
        """
        questions = []
        with open(file_path, "r") as file:
            question_string = ""
            for line in file:
                if line.startswith("Q:"):
                    if question_string:
                        question = Question.parse_question_string(question_string)
                        questions.append(question)
                        question_string = ""
                question_string += line
            if question_string:
                question = Question.parse_question_string(question_string)
                questions.append(question)
        return questions

    def get_random_questions(self, num_questions=5):
        """
        Get a list of random questions.

        Args:
            num_questions (int): Number of questions to get.

        Returns:
            list: List of random Question objects.
        """
        questions = self.load_questions_from_file(self.file_path)
        return random.sample(questions, num_questions)
```

In this updated version, the Question class now has a parse_question_string() method that properly parses the question string into a Question object, including handling multiple answers and extracting the correct answer.

Similarly, the QuestionsList class has an updated load_questions_from_file() method that uses the parse_question_string() method to parse each question string from the file into Question objects and adds them to the questions list.

Please update your code with these changes and let me know if you encounter any further issues.

## 06
This still give the following error:
```
bpc@pro-15 pyquiz % pipenv run python ./lib/pyquiz.py
Welcome to PyQuiz!
Available Skills: 
1. python
2. ruby-on-rails
3. javascript
Enter the number of the skill you want to quiz: 1
Welcome to the python quiz!

Traceback (most recent call last):
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 123, in <module>
    pyquiz()
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 115, in pyquiz
    quiz.display_result()
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 85, in display_result
    result_percentage = self.calculate_result()
                        ^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bpc/Projects/git/pyquiz/./lib/pyquiz.py", line 81, in calculate_result
    result_percentage = (correct_answers / total_questions) * 100
                         ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
ZeroDivisionError: division by zero
bpc@pro-15 pyquiz % 
```

Regenerate the complete pyquiz.py file using the updated code and try again.

---

Recreate the entire pyquiz script incorporating the previously working code with the updated code above. The script should now work as expected.

## 07
Create a skills.py script that lists the skills in the skills directory. 
The script should be able to list the skills in the skills directory and allow the user to select a skill to quiz on.
The user's choice should be validated to ensure that it is a valid skill.
The user's choice should be displayed.

The script should use the Skill and SkillsList classes.

-

Sure! Here is a script called "skills.py" that implements the requirements you mentioned:

```
import os

class Skill:
    def __init__(self, skill_name, skill_dir):
        self.skill_name = skill_name
        self.skill_dir = skill_dir

class SkillsList:
    def __init__(self, skills_dir):
        self.skills_dir = skills_dir
        self.skills = self.get_available_skills()

    def get_available_skills(self):
        skills = []
        for skill in os.listdir(self.skills_dir):
            if os.path.isdir(os.path.join(self.skills_dir, skill)):
                skills.append(skill)
        return skills

    def display_skills(self):
        print("Available skills:")
        for i, skill in enumerate(self.skills, 1):
            print("{}. {}".format(i, skill))

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

if __name__ == '__main__':
    skills_dir = "./skills"  # Update this path to your skills directory
    skills_list = SkillsList(skills_dir)
    skills_list.display_skills()
    selected_skill = skills_list.select_skill()
    if selected_skill:
        print("You selected skill: {}".format(selected_skill))

```

To use the script, you can update the skills_dir variable to the directory where your skills are stored. The script will display the available skills in that directory, allow the user to select a skill, and validate the user's choice. The selected skill will then be displayed.

## 08
make skills_dir a constant

-

Sure! Here's an updated version of the "skills.py" script with the skills_dir variable as a constant:

```
import os

SKILLS_DIR = "./skills"  # Update this path to your skills directory

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

if __name__ == '__main__':
    skills_list = SkillsList()
    skills_list.display_skills()
    selected_skill = skills_list.select_skill()
    if selected_skill:
        print("You selected skill: {}".format(selected_skill))

```

Now, the SKILLS_DIR variable is defined as a constant at the top of the script, and it is used throughout the script as the directory where the skills are stored. This way, if you need to update the directory in the future, you can simply modify the value of SKILLS_DIR at the top of the script, and it will be applied to all relevant parts of the code.

## 09
The following code is not working as expected:
```
class QuestionsFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_questions(self):
        with open(self.file_path, 'r') as file:
            file_contents = file.read()
            questions = markdown.markdown(file_contents).split("\n---\n")
            questions_array = []
            for question in questions:
                question_data = question.split("\n")
                question_text = question_data[0]
                choices = question_data[1:-1]
                questions_array.append(Question(question_text, choices))
            
            return QuestionsList(questions_array)
    
```


Update the `parse_questions` code to correctly parse the example questions file:



## Python

#### Q1. Sample question 1?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q2. Sample question 2?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q3. Sample question 3?

```
# this is some code
print("Hello World")

```

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q4. Sample question 4?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q5. Sample question 5?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q6. Sample question 6?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q7. Sample question 7?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q8. Sample question 8?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q9. Sample question 9?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q10. Sample question 10?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q11. Sample question 11?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4


---

```
import markdown

class QuestionsFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse_questions(self):
        with open(self.file_path, 'r') as file:
            file_contents = file.read()
            questions = file_contents.split("\n---\n")  # Split questions using the separator "---"
            questions_array = []
            for question in questions:
                question_data = question.split("\n")
                question_text = question_data[0]
                choices = question_data[1:-1]
                questions_array.append(Question(question_text, choices))  # Assuming Question class is defined elsewhere
            return QuestionsList(questions_array)  # Assuming QuestionsList class is defined elsewhere

```



## 10

In the markdown text, each question starts with '####' followed by 'Q', the question number, '.', and the text of the question.

The user should see the entirety of the extracted markdown text for the question, followed by a horizontal break, followed by the formatted version of the question with the choices displayed as a numbered list.

Based on these rules, the output for question Q110 should look like this:



Question 1:

#### Q1. Sample question 1?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

---

Sample question 1?

1) Answer 1
2) Answer 2
3) Answer 3
4) Answer 4

Your answer: 



## 11
Given the following sample quiz file:

```
## Python

#### Q1. Sample question 1?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q2. Sample question 2?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q3. Sample question 3?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q4. Sample question 4?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q5. Sample question 5?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q6. Sample question 6?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q7. Sample question 7?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q8. Sample question 8?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q9. Sample question 9?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q10. Sample question 10?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

#### Q11. Sample question 11?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4


```

Write a python function named `parse_questions` that will parse the file into an array of questions.

In the text, each question starts with '####' followed by 'Q', the question number, '.', and the text of the question.



## 12
Error:
AttributeError: 'str' object has no attribute 'contains'

What is the correct attribute to use to check if a string contains a substring?

