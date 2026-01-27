#This is the python file for the Week 02
import random

#This is the Code for the RockPaperScissors Game
def RockPaperScissors():
    options = ["Rock","Paper","Scissors"]
    playerChoice = input("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors\n: ")
    playerChoice = int(playerChoice)
    if playerChoice < 1 or playerChoice >3:
        print("Error: Choice must be between 1 and 3!")
    else:
        gameChoice = random.randint(1,3)
        playerChoice = options[playerChoice-1]
        gameChoice = options[gameChoice-1]
        if playerChoice == gameChoice:
            print(f"Tie: Both Players chose {playerChoice}")
        else:
            if(playerChoice == "Rock"):
                if(gameChoice == "Paper"):
                    whoWon(playerChoice,gameChoice, 1)
                else:
                    whoWon(playerChoice,gameChoice, 0)
            elif(playerChoice == "Paper"):
                if(gameChoice == "Scissors"):
                    whoWon(playerChoice,gameChoice, 1)
                else:
                    whoWon(playerChoice,gameChoice, 0)
            else:
                if(gameChoice == "Rock"):
                    whoWon(playerChoice,gameChoice, 1)
                else:
                    whoWon(playerChoice,gameChoice, 0)

# This is the code to choose who won the game
def whoWon(player,game, won):
    if(won == 1):
        print(f"Game Wins: Player chose {player}, Game chose {game}")
    else:
        print(f"Player Wins: Player chose{player}, Game chose {game}")

# This is the Menu to choose the game and choose to replay
while (True):
    menuChoice = input("Press 1 for Rock,Paper,Scissors\nPress 2 to Quit\n: ")
    menuChoice = int(menuChoice)
    if menuChoice == 1:
        RockPaperScissors()
    elif menuChoice == 2:
        break
    else:
        print("Error: Choice must be 1 or 2")