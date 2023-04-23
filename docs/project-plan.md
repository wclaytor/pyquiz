# pyquiz project plan
This original project plan was proposed by ChatGPT after some iteration on the project idea.

## Plan
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
