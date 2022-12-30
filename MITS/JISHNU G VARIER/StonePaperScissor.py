import random

def game():
  print("Rock-Paper-Scissors Game!!!")
  print("There are 3 choices:")
  print("  'R' for Rock")
  print("  'P' for Paper")
  print("  'S' for Scissors")
  print("Enter 'Q' to quit the game.\n")
  count=compcount=0
  
  while True:
    player= input("Enter your choice: ")
    player= player.upper()
    if player== 'Q':
      if count>compcount:
        print("You win!")
      elif count==0 and compcount==0:
        print("Exit")
        break
      elif count==compcount:
        print("It's a tie!")
      else:
        print("The computer wins!")
      print("Your score is",count,"and computer score is",compcount)
      print("Thank you...Exit")
      break

    #choosing random choice and score calculation

    X = random.choice(['R', 'P', 'S'])
    print("Computer move=",X)
    if player != 'R' and player != 'P' and player != 'S':
      print("Invalid move. Please try again.\n")
      continue
    if player == X:
          print("It's a tie!\n")
    elif (player == 'R' and X == 'S') or (player == 'P' and X == 'R') or (player == 'S' and X == 'P'):
          print("you scored 1\n")
          count+=1
    else:
          print("computer scored 1\n")
          compcount+=1

game()