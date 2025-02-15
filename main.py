import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
            (player == "paper" and computer == "rock") or \
            (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"


def play_game():
    print("\n🎮 Welcome to Rock-Paper-Scissors!")
    print("This game has 5 rounds, and your score will be tracked.")
    print("Press 'q' anytime to quit.\n")

    rounds = 0
    player_score = 0
    computer_score = 0
    ties = 0
    max_rounds = 5

    while rounds < max_rounds:
        print(f"🔵 Round {rounds + 1} of {max_rounds}")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice == "q":
            print("\n🚪 Exiting game... Thanks for playing! 👋")
            return

        if player_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Please choose 'rock', 'paper', or 'scissors'.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")

        result = get_winner(player_choice, computer_choice)

        if result == "win":
            player_score += 1
            print("🎉 You win this round!\n")
        elif result == "lose":
            computer_score += 1
            print("😢 You lose this round.\n")
        else:
            ties += 1
            print("🤝 It's a tie!\n")

        rounds += 1
        print(f"📊 Scoreboard: You {player_score} | Computer {computer_score} | Ties {ties}")
        print("-" * 40)

    print("\n🎯 Game Over! Here’s the final score:")
    print(f"✅ You: {player_score}")
    print(f"🤖 Computer: {computer_score}")
    print(f"⚖️ Ties: {ties}")

    if player_score > computer_score:
        print("🏆 Congratulations! You won the game! 🎉")
    elif player_score < computer_score:
        print("😢 The computer wins! Better luck next time.")
    else:
        print("🤝 It's a tie overall!")

    # Ask if the player wants to restart
    while True:
        play_again = input("\n🔄 Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            play_game()
            break
        elif play_again == "no":
            print("Thanks for playing! Goodbye. 👋")
            break
        else:
            print("❌ Invalid choice! Please type 'yes' or 'no'.")


if __name__ == "__main__":
    play_game()
