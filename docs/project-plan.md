# py-quiz notes

## Goal
Create a python script named pyquiz that quizzes the user based on a supplied list of questions.

## Background
* Skills
The directory `./skills` contains a subdirectory for each skill. 
Each subdirectory contains a file named `{$skill}-quiz.md` that contains a list of questions for that skill.

The script should ask the user to choose a skill from the list of skills in the `./skills` directory.

* Questions
The questions are in markdown format and the correct answer for each question is marked with an X.
The script should parse the questions file for the chosen skill and extract the questions into a list of questions.

* Quiz
The script should ask the user to choose 5 questions from the list at random.
The script should ask the user each question separately and record the user's answer.
The script should display the user's results at the end of the quiz.


## Specifications
The script should use the following classes:

Skill:
An area of knowledge in which to be quizzed
The quizzes directory contains one or more sub-directories with the name of each skill

QuestionsFile:
A markdown file containing the list of questions for a specified skill
The markdown file should be parsed into a list of Questions

Question:
An entity comprising the question itself along with examples, etc..., as well as the choices for the question and the correct answer

QuestionsList:
The list of questions extracted from the QuestionsFile for a specified Skill

Quiz:
The set of randomly chosen Questions for the specified Skill as well as the user specified answers and the overall result
The result should be displayed as a percentage of correct answers for the quiz
The pass / fail result should be displayed (75% = pass)

## User Stories
### 01

#### 01.01 - Choose a skill
As a user 
I want to select from a list of skills
So that I can practice a specific skill

#### 01.02 - Take a quiz
As a user
I want to take a quiz on a specific skill
So that I can practice the questions for that skill

#### 01.03 - Review results
As a user
I want to review my results at the end of the quiz
So that I know how I did

#### 01.04 - Practice a quiz
As a user
I want to practice a quiz on a specific skill
So that I can improve my results

#### 01.05 - Get a skill badge
As a user
I want to get a skill badge
So that I can show off my skills

