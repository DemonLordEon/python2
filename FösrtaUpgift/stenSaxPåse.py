import random

computure_score = 0
player_score = 0

options = ["rock", "paper", "scissors"]

while computure_score < 3 or player_score < 3:

    player = input("rock paper or Scissors: ").lower()

    computure = random.choice(options)

    print("player's turn:", player)

    print("computure's turn", computure)

    if player == computure:
        print("its a tie!",  player_score and computure_score)

    elif player == "rock" and computure == "scissors":
        player_score += 1
        computure_score = 0
        print("You win! ", player_score, "\n")

    elif player == "paper" and computure == "rock":
        player_score += 1
        computure_score = 0
        print("You win!", player_score, "\n")

    elif player == "scissors" and computure == "paper":

        player_score += 1
        computure_score = 0
        print("You win!", player_score, "\n")

    else:
        player_score = 0
        computure_score += 1
        print("computure wins!", computure_score, "\n")
