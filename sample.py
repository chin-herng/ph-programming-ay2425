import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
player_choice = input("Enter your choice (rock, paper, scissors): ")

if player_choice == "rock":
    if computer_choice == "rock":
        print("It's a tie!")
    elif computer_choice == "paper":
        print("Computer win!")
    else:
        print("You win!")
        
elif player_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    elif computer_choice == "paper":
        print("It's a tie!")
    else:
        print("Computer win!")
        
else: 
    if computer_choice == "rock":
        print("Computer win!")
    elif computer_choice == "paper":
        print("You win!")
    else:
        print("It's a tie!")