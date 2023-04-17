# py-quiz

## Specifications
This script will take a list of questions as input
The file is in markdown format
The correct answer for each question is marked with an X
The script will ask the user to choose a skill

## Classes
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

## Sample Questions

The file is in markdown format and the correct answer for each question is marked with an X.
There are 179 questions in the file currently but the contents of the file could change over time.
Therefore, the solution should take the file as input and not rely upon a fixed set of questions.
