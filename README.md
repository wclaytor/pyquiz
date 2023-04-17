# pyquiz
Turn markdown-based question lists into interactive quizzes

## About
pyquiz is a Python script that allows you to take practice quizzes and see your results. 

## How to use

### Install dependencies
```
pipenv install
```

### Run the script
```
pipenv run python ./src/pyquiz.py
```

## Skills
As we work to improve our skills, it is important to practice.

This script allows users to practice their skills by taking interactive quizzes based on markdown files.

### Quiz file format
Quiz files are markdown files that contain questions and answers.

#### Example quiz file:
```
# skill-name.md
## Skill Name

#### Q1. Sample question 1?

- [ ] Answer 1
- [ ] Answer 2
- [x] Answer 3
- [ ] Answer 4

```

### Example quiz files
The `./skills` directory contains example quiz files that you can use to try out pyquiz.
However, you can also use your own quiz files.

### Options
By default, the script will use the example quiz files found in the `./skills` directory.
If you would like to use your own collection of quiz files, you can update the `./src/pyquiz.py` file to enable user mode.

The `USER_MODE = False` line should be changed to `USER_MODE = True` and the `USER_SKILLS_DIR` and `USER_NUM_QUESTIONS` values should be updated to point to your own quiz files and the number of questions you would like to be asked.

For example, if your quiz files are located in a directory called `pyquiz-skills` that is adjacent to this project directory, and you would like to be asked 15 questions, your `./src/pyquiz.py` file should look like this:

```
# pyquiz.py

...

# To use your own settings, set USER_MODE to True
# Then set the USER_SKILLS_DIR and USER_NUM_QUESTIONS values below
USER_MODE = True
USER_SKILLS_DIR = "../pyquiz-skills"
USER_NUM_QUESTIONS = 15

```


## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

