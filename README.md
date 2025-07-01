# Calculator Application

---

# About Calculator

The Calculator application allows users to perform basic calculator operations that handle two operands.  
Users select the operations they want to perform using a command line prompt.  Other commands are available for additional features.  

## Supported Commands

Calculator supports two types of commands.

**Operational commands**
- Addition and Subtraction
- Multiplication and Division
- Exponentiation and Radication
- Division Remainder and Quotient
- Percentage
- Absolute Difference

**Functional commands**
- Show and Clear Calculation History
- Save and Load Calculation History
- Undo and Redo Calculations
- Display Help with Example Calculations
- Exit the Calculator

---

# Installation Instructions

> All commands performed from application directory.

**Set-up Python virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Install dependancies**

```bash
pip install -r requirements.txt
```

---

# Configuration Setup

> Configuration parameters are supported in a `.env` file.  If the file doesn't exist, you must first create it.

```bash
touch .env
```

## Supported Parameters

| Parameter                      | Use                                         |
|--------------------------------|---------------------------------------------|
| `CALCULATOR_LOG_DIR`           | Directory for log files.                    |
| `CALCULATOR_HISTORY_DIR`       | Directory for history files.                |
| `CALCULATOR_MAX_HISTORY_SIZE`  | Maximum number of history entries.          |
| `CALCULATOR_AUTO_SAVE`         | Auto-save flag. (`true` or `false`)             |
| `CALCULATOR_PRECISION`         | Number of decimal places for calculations.  |
| `CALCULATOR_MAX_INPUT_VALUE`   | Maximum allowed input value.                |
| `CALCULATOR_DEFAULT_ENCODING`  | Default encoding for file operations.       |

---

# Usage Guide

> Run Calculator Application

```bash
python3 main.py
```

Commands are entered at the `Enter command:` prompt.  There are two types of commands, **Operational commands** which perform mathematical operations and always ask 
for two numbers to be entered before providing a result, and **Functional commands** which require no additional inputs and perform an application function.  Typing `cancel`
when an operational command is prompting for a number will cancel that operation and return to the command prompt.

**Acceptable Operational Commands:**

| Command                  | Calculation performed          |
|--------------------------|--------------------------------|
| `add`                    | **Addition** of the two numbers.    |
| `subtract`               | **Subtraction** of one number from the other. |
| `multiply`               | **Multiplication** of the two numbers.   |
| `divide`                 | **Division** of one number from the other. |  
| `power`                  | **Exponentiation** of one number by the other. |
| `root`                   | **Radication** of one number from the other. |
| `modulus`                | Provides the **remainder** of dividing one number by the other. |
| `int_divide`             | Provided the **integer quotient** of dividing one number by the other. |
| `percent`                | **Percentage** of one number of the other. |
| `abs_diff`               | Returns the **absolute difference** of the two numbers. Describes how "far apart" the two numbers are. |

**Acceptable Functional Commands:**

| Command                  | Action performed          |
|--------------------------|--------------------------------|
| `history`                | **Shows** the calculation history.    |
| `clear`                  | **Clears** the calculation history. |
| `undo`                   | **Undoes** the last calculation, up to the first calculation performed during this active session.   |
| `redo`                   | **Redoes** the most recently undone calculation, up to any calculation undone during this session. |  
| `save`    | Manually **saves** the calculation history.  The history is automatically saved when you exit the session or after every calculation if auto-save is on. |
| `load`                   | **Load** the calculation history from file.  Effectively undoes all calculations since last save. |
| `help`                   | Displays a **help** of available commands. |
| `exit`                   | **Exits** the application gracefully. |

---

# Testing Instructions

## To run full suite of tests.

```bash
pytest
```

## To run individual test files.

```bash
pytest tests/<test_file.py>
```

**Individual Test Files Available**

| Test File Name            | What it Tests                        |
|---------------------------|---------------------------------------|
| `test_calculation.py`     | The `Calculation` object, which encapsulates the details of a single mathematical operation. | 
| `test_calculator_repl.py` | The `calculator_repl` function, which runs the **Read-Eval-Print Loop** that handles the command line. |
| `test_calculator.py`      | The `Calculator` object, which is the core of the calculator application. |
| `test_config.py`          | The `CalculatorConfig` object, which manages the configuration parameters. |
| `test_exceptions.py`      | The base `CalculatorError` exception, and the custom exceptions `OperationError`, `ValidationError` and `ConfigurationError` |
| `test_history.py`         | The `LoggingObserver` object, which logs calculations and the `AutoSaveObserver`, which auto-saves the calculation history. | 
| `test_memento.py`         | The `CalculatorMemento` object, which manages calculation history for undo and redo functions. |
| `test_operations.py`      | The `OperationFactory` object and all creatable `Operation` objects, which implements each of the mathematical operations. |
| `test_validators.py`      | The `InputValidator` object, which validates the operands provided for each calculation. |

---

# CI\CD Information

> GitHub Actions defined by `.github/workflows/python-app.yml` file.

```bash
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Run tests with pytest and enforce 90% coverage
      run: |
        pytest --cov=app --cov-fail-under=90
```

## GitHub Actions Steps

- **Check out code:** Using `actions/checkout` to access the Repository.
- **Set Up Python Environment:** Using `actions/setup_python` to specify Python version.
- **Install dependencies:** Install all required packages from `requirements.txt`.
- **Lint with flake8:** Analyze codebase for potential errors with `flake8`.
- **Run Tests and Enforce Coverage Threshold:** Ensure that the CI pipeline fails if test coverage falls below 90%.
