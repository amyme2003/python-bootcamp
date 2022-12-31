# Rock paper scissor game
from random import randint
# move for the players
moves = ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper or scissors? (or end the game)").lower()
    if player == "end the game":
        print("The Game has Ended.")
        break
    elif player == computer:
        print("Tie!")

     elif player == "rock":
        if computer == "paper":
            print("you lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)

    elif player == "paper":
        if computer == "Scissors":
                print("you lose!", computer, "beats", player)
        else:
                print("You win!", player, "beats", computer)

    elif player == "Scissors":
        if computer == "rock":
                print("you lose!", computer, "beats", player)
        else:
                print("You win!", player, "beats", computer)
    else:
        print("Check your spelling")

