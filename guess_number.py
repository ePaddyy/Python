import sys
import random
# import random
# from enum import Enum



def guess_number():
    game_count = 0
    player_wins = 0
    computer_wins = 0  
    player_win_percentage = 0
    computer_win_percentage = 0  

    def play_guess():
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal player_win_percentage
        nonlocal computer_win_percentage
        print("")

        playerchoice = input("Enter a number between 1 and 3:\n\n")
        computerchoice = random.randint(1, 3)

        player = int(playerchoice)
        computer = int(computerchoice)

        while True:
            try:
                if player < 1 or player > 3:
                    print("Enter a number between 1 and 3")
                    continue

                break

            except ValueError:
                print("Invalid input. Please enter a valid number.")

        print("")
        print(f"You chose {player}")
        print(f"Computer chose {computer}")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal player_win_percentage
            nonlocal computer_win_percentage

            if player == computer:
                player_wins += 1
                return "🎉 You win!"
            else:
                computer_wins += 1
                return "😢 Computer wins!"
            
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"\nGame Count: {str(game_count)}")
        print(f"\nPlayer Wins: {str(player_wins)}")
        print(f"\nComputer Wins: {str(computer_wins)}")

        player_win_percentage = (player_wins / game_count) * 100
        computer_win_percentage = (computer_wins / game_count) * 100
        print(f"\nPlayer Win Percentage: {player_win_percentage:.2f}%")
        print(f"Computer Win Percentage: {computer_win_percentage:.2f}%")

        print("")
        print("play again")
        while True:
            playagain = input("\nPlay again?\nY for Yes\nQ for Quit: ")

            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess()
        else:
            print("\n🎉🎉🎉🎉🎉🎉")
            print("Thank You for playing!\n")
            # sys.exit("Bye! 👋")
            return
        
    play_guess()

# guess_number()

if __name__ == "__main__":
    guess_number()
