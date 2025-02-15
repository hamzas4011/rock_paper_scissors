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


def main():
    print("🎮 Welcome to Rock-Paper-Scissors! 🎮")
    print("Type 'quit' to exit the game.\n")

    rounds = 0
    player_score = 0
    computer_score = 0
    ties = 0

    while True:
        print(f"🔵 Round {rounds + 1} 🔵")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice == "quit":
            print("\n📢 Final Score 📢")
            print(f"✅ You: {player_score}")
            print(f"🤖 Computer: {computer_score}")
            print(f"⚖️ Ties: {ties}")
            print("Thanks for playing! Goodbye. 👋")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Try again.\n")
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
        print("-" * 40)  # Separator for better readability


if __name__ == "__main__":
    main()

