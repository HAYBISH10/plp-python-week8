# Personal Mini-Toolkit
# PLP Python Final Project


# Tool 1: Simple Calculator
# This tool performs basic mathematical calculations.
def calculator():
    print("\n--- Simple Calculator ---")

    first_number = float(input("Enter the first number: "))
    operator = input("Enter an operation (+, -, *, /): ")
    second_number = float(input("Enter the second number: "))

    if operator == "+":
        result = first_number + second_number
        print(f"Result: {first_number} + {second_number} = {result}")

    elif operator == "-":
        result = first_number - second_number
        print(f"Result: {first_number} - {second_number} = {result}")

    elif operator == "*":
        result = first_number * second_number
        print(f"Result: {first_number} * {second_number} = {result}")

    elif operator == "/":
        if second_number != 0:
            result = first_number / second_number
            print(f"Result: {first_number} / {second_number} = {result}")
        else:
            print("Sorry, you cannot divide by zero.")

    else:
        print(f"Sorry, '{operator}' is not a valid operation.")


# Tool 2: To-Do List
# This tool allows the user to add, remove, and view tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' has been added.")

        elif choice == "2":
            task = input("Enter the task to remove: ")

            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' has been removed.")
            else:
                print("That task is not on your list.")

        elif choice == "3":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


# Tool 3: Number Guessing Game
# This tool keeps asking the user to guess a secret number until they are correct.
def guessing_game():
    secret_number = 7
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I have chosen a number between 1 and 20.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print(f"Congratulations! You guessed the number {secret_number}!")
            print(f"You got it in {attempts} tries!")
            break


# Main menu
print("========================================")
print("       WELCOME TO MY MINI-TOOLKIT")
print("========================================")
print("Choose a tool and let's get started!")

while True:
    print("\n========================================")
    print("       PERSONAL MINI-TOOLKIT")
    print("========================================")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("\nThank you for using my Personal Mini-Toolkit!")
        print("Goodbye! Have a great day!")
        break

    else:
        print(f"\nSorry, '{choice}' is not on the menu.")
        print("Please choose 1, 2, 3, or 4.")
