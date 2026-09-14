# plp-python-week8

# Personal Mini-Toolkit

## Project Description

The Personal Mini-Toolkit is a Python menu-driven program that combines several useful small tools in one application. It contains a Simple Calculator, a To-Do List, and a Number Guessing Game.

The project demonstrates Python variables, user input, conditionals, loops, lists, functions, and f-strings.

## Tools

### 1. Simple Calculator

The calculator performs addition, subtraction, multiplication, and division. It also checks for division by zero and invalid operations.

### 2. To-Do List

The To-Do List allows users to add tasks, remove tasks, and display their current tasks. It uses a Python list that changes while the program is running.

### 3. Number Guessing Game

The Number Guessing Game asks the user to guess a secret number between 1 and 20. It gives "Too high!" or "Too low!" hints and counts the number of attempts.

## How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal in the project folder.
3. Run the program using:

```bash
python toolkit.py
```

4. Choose a number from the main menu to use a tool.
5. Choose option 4 when you want to quit.

## Reflection

The hardest part of the project was connecting the different tools to one main menu while making sure the menu continued to appear after each tool finished. The bug that took the longest to fix was making sure the to-do list could safely remove an item without crashing when the item was not present. I solved this by checking whether the task was in the list before using `remove()`. I also had to make sure the guessing game changed its attempt counter and stopped when the correct number was entered. The project helped me understand how loops, lists, and conditionals can work together in a real program. If I had one more week, I would add a currency converter and a student grade calculator. I would also improve the program by saving the to-do list to a file so the tasks could be available the next time the program is opened.
