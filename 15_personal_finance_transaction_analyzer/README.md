# Personal Finance Transaction Analyzer

A command-line Python application for recording and analyzing personal financial transactions.

The program allows users to add income and expense transactions, view and filter transaction records, calculate financial statistics, analyze spending by category, and generate a complete financial summary.

## Features

* Add new transactions
* Record both income and expenses
* View all transactions
* Filter transactions by:

  * Category
  * Transaction type
* Calculate:

  * Total income
  * Total expenses
  * Current balance
* Find the largest expense
* Calculate spending by category
* Find the highest-spending category
* Generate a complete financial summary
* Validate user input using exception handling

## Transaction Structure

Each transaction stores information such as:

* Description
* Category
* Transaction type
* Amount

Example:

```python
{
    "description": "Rent",
    "category": "Housing",
    "type": "expense",
    "amount": 12000
}
```

Multiple transactions are stored in a list of dictionaries.

```python
transactions = [
    {
        "description": "Salary",
        "category": "Income",
        "type": "income",
        "amount": 45000
    },
    {
        "description": "Rent",
        "category": "Housing",
        "type": "expense",
        "amount": 12000
    }
]
```

## Planned Functions

The project will include functions responsible for:

* Adding transactions
* Viewing transactions
* Filtering transactions
* Calculating financial statistics
* Calculating spending by category
* Finding the highest-spending category
* Displaying a financial summary

## Example Summary

```text
========== FINANCIAL SUMMARY ==========

Total income: ₹45,000
Total expenses: ₹21,500
Current balance: ₹23,500

Largest expense:
Rent -> ₹12,000

Spending by category:
Housing -> ₹12,000
Food -> ₹4,500
Travel -> ₹3,000
Shopping -> ₹2,000

Highest spending category:
Housing
```

## Python Concepts Used

This project combines several Python fundamentals:

* Variables
* Strings
* Lists
* Dictionaries
* Tuples
* Nested data structures
* `for` loops
* `while` loops
* Conditional statements
* Functions
* Function return values
* `try` / `except`
* `break` and `continue`
* String methods
* Dictionary methods
* List methods
* `sum()`
* `len()`
* Searching and filtering data
* Basic calculations

## Learning Goals

The purpose of this project is to practice combining multiple Python concepts in one larger program.

It focuses on:

* Designing a program before writing code
* Choosing suitable data structures
* Breaking a larger problem into functions
* Working with lists of dictionaries
* Filtering and analyzing structured data
* Avoiding unnecessary repeated code
* Writing readable and maintainable Python

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python finance_transaction_analyzer.py
```

5. Follow the menu instructions displayed in the terminal.

## Project Status

🚧 Currently under development.

The project is being built step by step as part of Python fundamentals practice.
