# Record coverage of the unmodified starter suite BEFORE extending the tests.
# ORIGINAL statement coverage: ____%
# Use one decimal place.

from quiz_platform.assessment_engine.quiz_results import QuestionResult, QuizSection, summarise


def test_question_result():
    # Testing for one single question
    question = QuestionResult(3, 4)
    assert question.totals() == (3, 4)
    assert str(question) == '3/4'


def test_one_question_section():
    # Testing for one particular question in a section
    section = QuizSection([QuestionResult(3, 4)])
    assert section.totals() == (3, 4)
    assert str(section) == '[3/4]'
    assert summarise(section) == {
        'earned': 3, 'possible': 4, 'percentage': 75.0,
    }


def test_empty_section():
    # Testing a section that has no question
    section = QuizSection([])
    assert section.totals() == (0, 0)
    assert str(section) == '[]'
    assert summarise(section) == {
        'earned': 0, 'possible': 0, 'percentage': None,
    }


def test_two_questions_section():
    # Testing a section with 2 questions 
    section = QuizSection([
        QuestionResult(2, 5),
        QuestionResult(1, 3)
    ])
    assert str(section) == '[2/5, 1/3]'
    assert section.totals() == (3, 8)
    assert summarise(section) == {
        'earned': 3, 'possible': 8, 'percentage': 37.5
    }


def test_multiple_questions_section():
    # Testing a section with multiple questions
    section = QuizSection([
        QuestionResult(3, 4),
        QuestionResult(2, 3),
        QuestionResult(1, 2)
    ])
    assert str(section) == '[3/4, 2/3, 1/2]'
    assert section.totals() == (6, 9)
    assert summarise(section) == {
        'earned': 6, 'possible': 9, 'percentage': 6 * 100 / 9,
    }


def test_nested_sections():
    # Testing a big section that has more than one section within it
    section = QuizSection([
        QuizSection([QuestionResult(2, 4), QuestionResult(1, 2)]),
        QuestionResult(3, 4),
    ])
    assert str(section) == '[[2/4, 1/2], 3/4]'
    assert section.totals() == (6, 10)
    assert summarise(section) == {
        'earned': 6, 'possible': 10, 'percentage': 60.0,
    }


def test_two_sections_with_different_question_counts():
    quiz = QuizSection([
        QuizSection([
            QuestionResult(3, 4),
            QuestionResult(2, 3),
            QuestionResult(1, 2),
        ]),
        QuizSection([
            QuestionResult(4, 5),
            QuestionResult(1, 2),
        ]),
    ])

    assert str(quiz) == '[[3/4, 2/3, 1/2], [4/5, 1/2]]'
    assert quiz.totals() == (11, 16)
    assert summarise(quiz) == {
        'earned': 11, 'possible': 16, 'percentage': 68.75,
    }
