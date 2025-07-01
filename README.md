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

---

# Testing Instructions

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
