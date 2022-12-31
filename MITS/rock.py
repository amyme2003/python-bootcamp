import random

def rps_game():
  print("Lets play Rock-Paper-Scissors")
  print("Enter your choice")
  print("  'R' for Rock")
  print("  'P' for Paper")
  print("  'S' for Scissors")
  print("Enter 'Q' to quit the game.\n")
  c=count=0
  while True:
    player= input("Enter your move: ")
    player= player.upper()
    if player== 'Q':
      if c>count:
          print("You win!")
      elif c==0 and count==0:
          print("Exit")
          break
      elif c==count:
          print("It's a tie!")
      else:
          print("C
                +omputer wins!")
      print("Your score is",c,"and computer score is",count)
      print("Thank you for playing! Exit.")
      break
    
    computer_move = random.choice(['R', 'P', 'S'])
    print("Computer move=",computer_move)
    if player != 'R' and player != 'P' and player != 'S':
      print("Invalid move. Please try again.\n")
      continue
    if player == computer_move:
          print("It's a tie!\n")
    elif (player == 'R' and computer_move == 'S') or (player == 'P' and computer_move == 'R') or (player == 'S' and computer_move == 'P'):
          print("you score 1\n")
          c+=1
    else:
          print("computer score 1\n")
          count+=1

rps_game()
