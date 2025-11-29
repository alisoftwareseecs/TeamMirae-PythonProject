def Muhammad_Ali():
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        print("Result:", num1, "+", num2, "=", num1 + num2)

    elif op == '-':
        print("Result:", num1, "-", num2, "=", num1 - num2)

    elif op == '*':
        print("Result:", num1, "*", num2, "=", num1 * num2)

    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero will result in an infinite number.")
        else:
            print("Result:", num1, "/", num2, "=", num1 / num2)

    else:
        print("Invalid operator used")


Muhammad_Ali()

import random

def Sajeel_Nadeem():
    play_again = "yes"

    for _ in range(100):  # Just a large loop so game can restart
        if play_again.lower() != "yes":
            break

        secret = random.randint(1, 50)
        attempts = 0
        print("\nThink of a number between 1 and 50:\n")

        for _ in range(100):  # Loop for guessing
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess > secret:
                print("Too high!")    # This will indicate that the number is higher
            elif guess < secret:
                print("Too low!")     # This will indicate that the number is lower
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        play_again = input("\nDo you want to play again? (yes/no): ")

Sajeel_Nadeem()