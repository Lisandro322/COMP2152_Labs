#This is the python file for the Week 02
import random
def RockPaperSissors():
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
                    print(f"Game Wins: Player chose {playerChoice}, Game chose {gameChoice}\n")
                else:
                    print(f"Player wins: Player chose {playerChoice}, Game chose {gameChoice}\n")
            elif(playerChoice == "Paper"):
                if(gameChoice == "Scissors"):
                    print(f"Game Wins: Player chose {playerChoice}, Game chose {gameChoice}\n")
                else:
                    print(f"Player wins: Player chose {playerChoice}, Game chose {gameChoice}\n")
            else:
                if(gameChoice == "Rock"):
                    print(f"Game Wins: Player chose {playerChoice}, Game chose {gameChoice}\n")
                else:
                    print(f"Player wins: Player chose {playerChoice}, Game chose {gameChoice}\n")

while (True):
    menuChoice = input("Press 1 for Rock,Paper,Scissors\nPress 2 to Quit\n: ")
    menuChoice = int(menuChoice)
    if menuChoice == 1:
        RockPaperSissors()
    elif menuChoice == 2:
        break
    else:
        print("Error: Choice must be 1 or 2")