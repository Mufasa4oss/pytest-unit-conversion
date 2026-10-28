# Basic Exploration of pytest

A small Python project I built to get hands-on with automated testing using pytest. Test temperature conversions and parsing results.

This is a learning project, focused on testing.

```
pyTest/
├── validator/          # The program being tested
│   ├── __init__.py
│   ├── parsing.py      # Splits a raw line like "TEMP01,72.5,F" into its parts
│   └── convertTemps.py # Converts between units (F/C/K)
└── tests/              # Tests for each module
    ├── test_parsing.py
    └── test_convertTemps.py
```

## How to use

1. Clone the repo: `git clone https://github.com/Mufasa4oss/pytest-unit-conversion.git`
2. Install pytest: `python -m pip install pytest`
3. Run the tests: `python -m pytest`

## Considerations

Use `pytest.approx` when comparing non-integer values. Example: `assert result == pytest.approx(32)`

### Bugs caught by tests

**1. Invalid-unit check rejected every conversion**

An early version validated units with:

    if from_unit or to_unit not in temps:

Python reads this as `from_unit or (to_unit not in temps)`. Since `from_unit` is a non-empty string, the first half is always true, so the function raised a `ValueError` on every call, including valid ones like `convert(0, "C", "F")`. The existing conversion tests failed immediately with `ValueError: C and/or F is invalid`, which pointed straight at the check.

Fix: check each unit separately.

    if (from_unit not in temps) or (to_unit not in temps):
