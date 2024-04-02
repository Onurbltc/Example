import random
import pandas as pd

options = ["rock","paper","scissors"]

play_again = True

while play_again:

    user_choice = input("Enter a choice(rock,paper,scisssors): ").lower()

    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(options)
    
    print(f"You chose {user_choice}, computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        play_again = True

    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        play_again = False

    else:
        print("You lose.")
        play_again = False


