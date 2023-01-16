from random import randint

t = ["rock", "paper", "scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
  player = input("rock, paper, scissors? ")
  if player == computer:
    print("Tie!")
  elif player == "rock":
    if computer == "paper":
      print("You lose!", computer, "covers", player)
    else :
      print("You win!", player, "smashes", computer)
  elif player == "paper":
    if computer == "scissors":
      print("You lose!", computer, "cuts", player)
    else:
      print("You win!", player, "covers", computer)
  elif player == "scissors":
    if computer == "rock":
      print("You lose!", computer, "smashes", player)
    else:
      print("You win!", player, "cuts", computer)
  elif player == "kaas":
    print("You win", player, "always wins")
  else:
    print("Check your spelling")
  player = False
  computer = t[randint(0,2)]
