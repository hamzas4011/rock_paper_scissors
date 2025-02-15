import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"


def main():
    print("Welcome to Rock-Paper-Scissors! Type 'quit' to exit.")

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice == "quit":
            print("Thanks for playing! Goodbye.")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = get_winner(player_choice, computer_choice)
        print(result)
        print("-" * 30)  # Separator for better readability


if __name__ == "__main__":
    main()
