# 🎯 Number Guessing Tournamentb

A fun command-line game built with Python where the player tries to guess a randomly generated number between 1 and 100.

The game provides hints after each incorrect guess and tracks the player's performance across multiple rounds.

## 🚀 Features

- 🎲 Generates a random number between 1 and 100
- 🔢 Allows the player to keep guessing until they find the correct number
- ⬆️ Gives a hint when the guess is too low
- ⬇️ Gives a hint when the guess is too high
- 🔄 Supports multiple rounds
- 🔢 Counts the number of attempts in each round
- 📊 Displays tournament statistics
- 🏆 Shows the best round with the fewest attempts
- ⚠️ Handles invalid input

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Navigate to the project directory

```bash
cd your-repository-name
```

### 3. Run the program

```bash
python filename.py
```

> Replace `your-username`, `your-repository-name`, and `filename.py` with your actual GitHub username, repository name, and Python filename.

## 🎮 How to Play

1. The program generates a random secret number between 1 and 100.
2. Enter a number as your guess.
3. The program tells you whether your guess is too high or too low.
4. Keep guessing until you find the correct number.
5. Your number of attempts is recorded for that round.
6. Choose whether you want to play another round.
7. When you finish playing, the program displays your tournament statistics.

## 📊 Tournament Statistics

At the end of the game, the program displays:

- Total rounds played
- Total attempts
- Average attempts per round
- Best round with the fewest attempts

### Example

```text
=== Tournament Results ===
Rounds played: 3
Total attempts: 12
Average attempts per round: 4.0
Best round: 3 attempts
```

## 🧠 Concepts Used

This project practices several Python fundamentals:

- Variables and data types
- User input and type conversion
- Conditional statements
- `while` loops
- Functions
- Lists
- Counters
- Exception handling with `try` and `except`
- The `random` module
- Loops and calculations

## 📚 Learning Goals

Through this project, I practiced:

- Building an interactive command-line game
- Using loops to control program flow
- Tracking information across multiple rounds
- Storing and processing data in lists
- Handling invalid user input
- Breaking a program into smaller functions
- Generating random values
- Calculating basic statistics

---

**Note:** This is a command-line project and requires Python to be installed to run.
