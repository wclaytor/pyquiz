# test/tests/test_pyquiz.py

import unittest
from unittest.mock import patch

# pyquiz
from src.pyquiz import Skill, SkillsList, Question, QuestionsFile

class TestSkill(unittest.TestCase):
    def test_init(self):
        skill = Skill("skill_name", "skill_dir")
        self.assertEqual(skill.skill_name, "skill_name")
        self.assertEqual(skill.skill_dir, "skill_dir")

class TestSkillsList(unittest.TestCase):
    def test_get_available_skills(self):
        skills_list = SkillsList()
        self.assertGreater(len(skills_list.get_available_skills()), 0)

    def test_display_skills(self): 
        skills_list = SkillsList()
        with patch('builtins.print') as mocked_print:
            skills_list.display_skills()
            mocked_print.assert_called()

    def test_select_skill_valid_choice(self):
        skills_list = SkillsList()
        with patch('builtins.input', return_value='1'):
            self.assertEqual(skills_list.select_skill(), skills_list.skills[0])

    def test_select_skill_quit_choice(self):
        skills_list = SkillsList()
        with patch('builtins.input', return_value='q'):
            self.assertEqual(skills_list.select_skill(), None)

    def test_select_skill_invalid_choice(self):
        skills_list = SkillsList()
        with patch('builtins.input', side_effect=['0', 'a', '100', 'q']):
            self.assertEqual(skills_list.select_skill(), None)

class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.question_text = "#### Q1. What is the capital of France?\n\n- [x] Paris\n- [ ] London\n- [ ] Berlin\n- [ ] Madrid\n"
        self.question = Question(self.question_text)

    def test_parse_question(self):
        self.assertEqual(self.question.heading, "What is the capital of France?")
        self.assertEqual(self.question.choices, ["Paris", "London", "Berlin", "Madrid"])

    def test_parse_heading(self):
        self.assertEqual(self.question.heading, "What is the capital of France?")

    def test_parse_untitled_heading(self):
        question_text = "#### Q1\n\n- [x] Paris\n- [ ] London\n- [ ] Berlin\n- [ ] Madrid\n"
        question = Question(question_text)
        self.assertEqual(question.heading, "Untitled Question")

    def test_parse_contents(self):
        self.assertEqual(self.question.contents, [''])

    def test_parse_choices(self):
        self.assertEqual(self.question.choices, ["Paris", "London", "Berlin", "Madrid"])

    def test_parse_multi_line_choices(self):
        # the full question text
        question_text = """
#### Q123. This is a question with a multi-line choice

```python
# some code

```

- [x] A

```python
# some code

```

- [ ] B

```python
# some code

```

- [ ] C

```python
# some code

```

- [ ] D

```python
# some code

```

**Explanation:** This is some crazy code!

[Reference](http://www.example.com)

"""
        
        question = Question(question_text)

        choice_text_A = """A

```python
# some code

```"""

        choice_text_B = """B

```python
# some code

```"""

        choice_text_C = """C

```python
# some code

```"""

        choice_text_D = """D

```python
# some code

```"""

        # self.assertEqual(question.choices, [
        #     choice_text_A,
        #     choice_text_B,
        #     choice_text_C,
        #     choice_text_D
        # ])

        self.assertEqual(question.choices[0], choice_text_A)
        self.assertEqual(question.choices[1], choice_text_B)
        self.assertEqual(question.choices[2], choice_text_C)
        self.assertEqual(question.choices[3], choice_text_D)

class TestQuestionsFile(unittest.TestCase):
    def test_parse_questions(self):
        file_path = "./skills/python/python-quiz.md"
        questions_file = QuestionsFile(file_path)
        self.assertGreater(len(questions_file.parse_questions()), 0)

if __name__ == '__main__':
    unittest.main()