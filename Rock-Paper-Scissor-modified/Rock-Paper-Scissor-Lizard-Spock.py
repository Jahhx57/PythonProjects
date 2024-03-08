import random

def play_round():
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user_input == "q":
        return None  # Indicates quitting

    if user_input not in options:
        print("Invalid input. Please enter Rock, Paper, Scissors, Lizard, Spock, or Q to quit.")
        return play_round()  # Recursive call to play_round

    random_number = random.randint(0, 4)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        return "Tie"

    # Define the winning conditions for Rock, Paper, Scissors, Lizard, Spock
    winning_conditions = {
        ("rock", "scissors"), ("rock", "lizard"),
        ("paper", "rock"), ("paper", "spock"),
        ("scissors", "paper"), ("scissors", "lizard"),
        ("lizard", "spock"), ("lizard", "paper"),
        ("spock", "scissors"), ("spock", "rock")
    }

    if (user_input, computer_pick) in winning_conditions:
        print("You won!")
        return "User"

    print("You lost!")
    return "Computer"

options = ["rock", "paper", "scissors", "lizard", "spock"]

def play_game(rounds_to_win):
    user_wins = 0
    computer_wins = 0

    for round_number in range(1, rounds_to_win + 1):
        print(f"\nRound {round_number}:")

        result = play_round()

        if result is None:
            print("Game aborted. Goodbye!")
            return

        if result == "User":
            user_wins += 1
        elif result == "Computer":
            computer_wins += 1
        else:
            print("It's a tie!")

        print(f"Score - You: {user_wins}, Computer: {computer_wins}")

    if user_wins > computer_wins:
        print("You won the game!")
    elif computer_wins > user_wins:
        print("The computer won the game!")
    else:
        print("The game ended in a tie!")

    play_additional_rounds(user_wins, computer_wins)

def play_additional_rounds(user_total_wins, computer_total_wins):
    while True:
        play_more = input("Do you want to play additional rounds? (yes/no): ").lower()
        if play_more == "yes":
            try:
                rounds_to_play = int(input("Enter the number of additional rounds to play: "))
                if rounds_to_play <= 0:
                    print("Please enter a positive number of rounds.")
                    continue
                user_wins, computer_wins = play_game(rounds_to_play)
                user_total_wins += user_wins
                computer_total_wins += computer_wins
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif play_more == "no":
            display_final_result(user_total_wins, computer_total_wins)
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def display_final_result(user_total_wins, computer_total_wins):
    print("\nFinal Results:")
    print(f"You won a total of {user_total_wins} rounds.")
    print(f"The computer won a total of {computer_total_wins} rounds.")
    
    if user_total_wins > computer_total_wins:
        print("Congratulations! You are the overall winner!")
    elif computer_total_wins > user_total_wins:
        print("The computer is the overall winner. Better luck next time!")
    else:
        print("The overall game ended in a tie!")

# Default is best of 5, with an option to go for best of 9
play_game(rounds_to_win=5)
