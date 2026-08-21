import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0
    player_win_percentage = 0
    computer_win_percentage = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal player_win_percentage
        nonlocal computer_win_percentage

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # while True:

        print("")
        
        playerchoice = input(
            "Enter.... \n1 for rock \n2 for paper \n3 for scissors:\n\n"
        )

        # try:
        #     player = int(playerchoice)
        # except ValueError:
        #     print("Invalid input. Please enter a number from 1 to 3.")
            

        if playerchoice not in ["1", "2", "3"]:
            print("Invalid Input")
            print("Try again. Enter a number from 1 to 3")
            return play_rps()

        player = int(playerchoice)
        computerchoice = random.choice("123")
        computer= int(computerchoice)

        print("")
        print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
        print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "😲 Tie!"
            else:
                computer_wins += 1
                return "😞 You lose! Computer wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame Count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nComputer wins: " + str(computer_wins))

        player_win_percentage = (player_wins / game_count) * 100 if game_count > 0 else 0
        computer_win_percentage = (computer_wins / game_count) * 100 if game_count > 0 else 0

        print(f"\nPlayer Win Percentage: {player_win_percentage:.2f}%")
        print(f"Computer Win Percentage: {computer_win_percentage:.2f}%")

        print("play again")

        while True:
            playagain = input("\nPlay again?\nY for Yes\nQ for Quit: ")

            if playagain.lower() not in ["y", "q"]:
                continue

            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉🎉🎉")
            print("Thank You for playing!\n")
            # sys.exit("Bye! 👋")
            return

    play_rps()
# rps()
                
if __name__ == "__main__":
    rps()
