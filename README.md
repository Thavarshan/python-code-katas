# Code Katas with Python Unittest

## Introduction

If martial artists use kata as a method for exercise and practice, what might be the equivalent for coders like us? Coding katas are short, repeatable programming challenges which are meant to exercise everything from your focus, to your workflow.

This was already done in PHPUnit which you can find [here](https://github.com/Thavarshan/phpunit-code-katas), so this time I'm doing it in Python.

## Katas

- Prime Factors
- Roman Numerals
- Bowling Game
- String Calculator
- Tennis Match
- FizzBuzz
- The Gilded Rose

## Installation

### Prerequisites

To run this project, you must have Python 3.6 or higher installed.

Begin by cloning this repository to your machine, and installing all dependencies dependencies.

### Get Started

```bash
git clone git@github.com:Thavarshan/python-code-katas.git katas
cd katas && pip install -r requirements.txt
```

## Testing

Just run Python unit test in the project root.

```bash
cd katas
python -m venv ./venv
source ./venv/bin/activate
python -m unittest discover tests -p '*_test.py'
```
