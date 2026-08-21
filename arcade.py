from RPS import rps
from guess_number import guess_number

def main():
    while True:
        print("Welcome to the Arcade!")
        print("Choose a game to play:")
        print("1. Rock, Paper, Scissors")
        print("2. Guess the Number")
        print("3. Exit")

        choice = input("Enter the number of the game you want to play (1, 2, or 3): ")

        if choice == "1":
            rps()
            
        elif choice == "2":
            guess_number()

        elif choice == "3":
            print("Exiting the Arcade. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    # print("Welcome to the Arcade!")
    # print("Choose a game to play:")
    # print("1. Rock, Paper, Scissors")
    # print("2. Guess the Number")
    # print("3. Exit")

    # while True:
    #     choice = input("Enter the number of the game you want to play (1, 2, or 3): ")

    #     if choice == "1":
    #         rps()
            
    #     elif choice == "2":
    #         guess_number()

    #     elif choice == "3":
    #         print("Exiting the Arcade. Goodbye!")
    #         break
    #     else:
    #         print("Invalid choice. Please enter 1, 2, or 3.")
# main()
if __name__ == "__main__":
    main()
# if __name__ == "__main__":
#     main()