# 🐍 Python Mini Projects

A collection of beginner-to-intermediate Python CLI projects built while learning core programming concepts.
Each project is self-contained and runnable from the terminal with no external dependencies.

---

## 📁 Projects

### 1. 📝 Todo List CLI App — `todo_cli_app.py`

A command-line task manager that saves your to-do list to a local text file so your tasks persist between sessions.

**Features:**
- View your current task list on startup
- Add new tasks (appended to file)
- Delete completed tasks by name
- Data is saved to `todo_list.txt` automatically

**How to run:**
```bash
# Make sure todo_list.txt exists in the same folder first
python todo_cli_app.py
```

**Example session:**
```
your current todo list is:
Buy groceries
Study Python

what you want to do add or delete tasks
please enter: add
input task that you want to add: Finish assignment
update list successfully
```

**Concepts used:** File I/O, string manipulation, conditional logic, user input handling

---

### 2. 🔐 Password Generator — `password_generator.py`

Generates a cryptographically secure random password using Python's `secrets` module.

**Features:**
- Uses `secrets.choice()` for secure randomness (safer than `random`)
- Combines letters and digits to form a strong password
- Configurable length (default: 10 characters)

**How to run:**
```bash
python password_generator.py
```

**Example output:**
```
aB3kR7mNpQ
```

**Concepts used:** `secrets` module, `string` module, list comprehension, secure random generation

---

### 3. 🌡️ Temperature Converter — `temp_convrt.py`

Converts temperatures between Celsius, Fahrenheit, and Kelvin from the command line.

**How to run:**
```bash
python temp_convrt.py
```

**Concepts used:** Functions, arithmetic operations, input validation, user menus

---

### 4. 🎲 Number Guessing Game — `number_guess_game.py`

A classic guessing game where the user tries to guess a randomly generated number with hints provided after each attempt.

**How to run:**
```bash
python number_guess_game.py
```

**Concepts used:** `random` module, loops, conditionals, input handling

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed — all standard library

---

## 🚀 How to Clone & Run

```bash
git clone https://github.com/Talha8899/python-mini-projects.git
cd python-mini-projects
python <filename>.py
```

---

## 👨‍💻 Author

**Talha Abdul Sattar**
- GitHub: [@Talha8899](https://github.com/Talha8899)
- LinkedIn: [talha-abdul-sattar-4b4926389](https://www.linkedin.com/in/talha-abdul-sattar-4b4926389)
- Email: talhaabdulsattar65@gmail.com

---

## 📌 About This Repo

These projects were built as part of my Python learning journey during myLearning journey at The Islamia University of Bahawalpur.
I'm actively working towards contributing to open-source projects through **Google Summer of Code 2026**.
