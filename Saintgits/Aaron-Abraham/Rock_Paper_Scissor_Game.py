import random

# Constants for the options
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

# Function to play the game
def play_game():
    # Generate a random choice for the computer
    computer_choice = random.choice([ROCK, PAPER, SCISSORS])

    # Get the user's choice
    user_choice = input("Enter your choice ({}/{}/{}): ".format(ROCK, PAPER, SCISSORS))

    # Check who wins the game
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == ROCK and computer_choice == SCISSORS:
        result = "You win!"
    elif user_choice == PAPER and computer_choice == ROCK:
        result = "You win!"
    elif user_choice == SCISSORS and computer_choice == PAPER:
        result = "You win!"
    else:
        result = "You lose!"

    # Print the result
    print("Computer chose:", computer_choice)
    print(result)

# Play the game multiple times
while True:
    play_game()
    play_again = input("Play again (y/n)? ")
    if play_again != "y":
        break
