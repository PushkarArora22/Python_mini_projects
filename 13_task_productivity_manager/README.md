# 📝 Task Manager

A simple command-line **Task Manager** built with Python. The application allows users to add, view, search, filter, complete, and remove tasks through an interactive menu.

This project was created to practice Python fundamentals and understand how different concepts can work together in a functional program.

## 🚀 Features

- ➕ Add new tasks
- 📋 View all tasks with their current status
- 🔍 Search tasks using keywords
- 🔎 Filter tasks by status (`Pending` or `Completed`)
- ✅ Mark tasks as completed
- 🗑️ Remove tasks
- ⚠️ Handle invalid task number input
- 🚪 Exit the application

## 🖥️ Example Task Structure

Each task is stored as a list containing the task name and its status:

```python
["Learn Python", "Pending"]
```

Multiple tasks are stored in a nested list:

```python
tasks = [
    ["Learn Python", "Pending"],
    ["Practice SQL", "Completed"],
    ["Build a Project", "Pending"]
]
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Navigate to the project directory

```bash
cd 13_task_productivity_manager
```

### 3. Run the program

```bash
python task_productivity_manager.py
```


## 🧠 Concepts Used

This project uses several Python fundamentals:

- Variables and data types
- Lists and nested lists
- List indexing
- List methods such as `append()` and `pop()`
- `for` and `while` loops
- Functions
- Conditional statements
- String methods such as `lower()` and `strip()`
- User input
- Type conversion
- Exception handling with `try` and `except`

## 📋 How the Application Works

When the program starts, it displays a menu with different options. The user selects an option, performs an action, and can continue using the application until choosing to exit.

The application keeps running using a loop, while individual functions handle specific tasks such as adding, searching, filtering, completing, or removing tasks.

## 📚 Learning Outcomes

Through this project, I practiced:

- Breaking a larger problem into smaller functions
- Working with nested lists
- Accessing and modifying list elements
- Validating user input
- Handling errors without crashing the program
- Building a simple menu-driven application

## 🔮 Future Improvements

Possible improvements for future versions include:

- 💾 Saving tasks to a file
- 📅 Adding due dates
- ⭐ Adding task priorities
- ✏️ Editing existing tasks
- 📊 Adding detailed task statistics

---

**Note:** Tasks are currently stored only while the program is running. Closing the application will reset the task list.
