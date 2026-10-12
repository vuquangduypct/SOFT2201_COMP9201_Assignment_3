# Record coverage of the unmodified starter suite BEFORE extending the tests.
# ORIGINAL branch coverage: ____%
# Use one decimal place.

from quiz_platform.assessment_engine.result_adapters import (
    Result, NativeResults, PercentageExport, PercentageAdapter,
    build_report,
)


def test_report_from_native_results():
    source = NativeResults([Result('Q-1', 3, 4)])
    assert build_report(source) == {
        'earned': 3, 'possible': 4, 'percentage': 75.0,
    }

def test_report_zeroscore():
    source = NativeResults([Result('Q-1', 0, 4)])
    assert build_report(source) == {
        'earned': 0, 'possible': 4, 'percentage': 0
    }

def test_report_from_percentage_adapter():
    payload = {
        'questions': [
            {'id': 'Q-1', 'weight': 4},
            {'id': 'Q-2', 'weight': 6},
        ],
        'submissions': {
            'Q-1': 75,  # 75% of 4 = 3
            'Q-2': 50,  # 50% of 6 = 3
        },
    }
    source = PercentageAdapter(PercentageExport(payload))
    assert build_report(source) == {
        'earned': 6, 'possible': 10, 'percentage': 60.0,
    }

def test_report_from_percentage_adapter_full_score():
    payload = {
        'questions': [{'id': 'Q-1', 'weight': 4}],
        'submissions': {'Q-1': 100},
    }

    source = PercentageAdapter(PercentageExport(payload))
    assert build_report(source) == {
        'earned': 4, 'possible': 4, 'percentage': 100.0,
    }


def test_report_from_percentage_adapter_missing_submission():
    payload = {
        'questions': [
            {'id': 'Q-1', 'weight': 4},
            {'id': 'Q-2', 'weight': 6},
        ],
        'submissions': {
            'Q-1': 75, # 75% of 4 = 3
            # Q-2 is missing, so earned = 0 for Q-2
        },
    }
    source = PercentageAdapter(PercentageExport(payload))

    assert build_report(source) == {
        'earned': 3, 'possible': 10, 'percentage': 30.0,
    }


def test_report_noquestions():
    source = NativeResults([])
    assert build_report(source) == {
        'earned': 0, 'possible': 0, 'percentage': None,
    }

def test_report_noquestions_percentage_adapter():
    payload = {
        'questions': [],
        'submissions': {},
    }
    source = PercentageAdapter(PercentageExport(payload))
    assert build_report(source) == {
        'earned': 0, 'possible': 0, 'percentage': None,
    }


# FILL IN: Add more tests to achieve 100% statement and branch coverage of result_adapters.py. 
# Add more test functions to this file
