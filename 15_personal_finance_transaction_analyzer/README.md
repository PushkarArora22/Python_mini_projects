# Personal Finance Analyzer

A simple Python-based personal finance analyzer that allows users to record, view, filter, and analyze their income and expenses.

## Features

* Add income and expense transactions
* View all recorded transactions
* Filter transactions by:

  * Category
  * Transaction type
* Calculate financial statistics:

  * Total income
  * Total expenses
  * Current balance
  * Largest expense
* Calculate total spending for a selected category
* Find the category with the highest total spending
* Generate a financial summary

## How It Works

Each transaction is stored as a dictionary inside a list.

A transaction contains:

```python
{
    "description": "Groceries",
    "category": "Food",
    "type": "expense",
    "amount": 500
}
```

The program then uses functions, loops, conditions, lists, and dictionaries to process and analyze the transactions.

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run:

```bash
python personal_finance_analyzer.py
```

## Example

```text
========== PERSONAL FINANCE ANALYZER ==========

1. Add transaction
2. View transactions
3. Filter transactions
4. Financial statistics
5. Spending by category
6. Highest spending category
7. Financial summary
8. Exit
```

## Project Purpose

This project was created to practice Python fundamentals by combining multiple concepts into a single practical application. It focuses on working with lists and dictionaries, looping through data, creating functions, filtering information, and performing basic financial calculations.

## Future Improvements

* Better input validation
* More formatted transaction output
* Ability to edit or delete transactions
* Saving transactions to a file
* Loading previously saved transactions
* More detailed financial reports

## Author

**Pushkar Arora**
