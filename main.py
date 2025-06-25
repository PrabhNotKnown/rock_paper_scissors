import random

# Map user input (both full word & shortcuts) to actual choice
input_map = {
    "rock": "rock",
    "r": "rock",
    "paper": "paper",
    "p": "paper",
    "scissors": "scissors",
    "s": "scissors"
}

# Emoji for each choice
emoji = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

def game():
    while True:
        you = input("Choose rock ✊, paper ✋ or scissors ✌️ (or r/p/s): ").lower()

        if you in input_map:
            you = input_map[you]
        else:
            print("❌ Invalid option!")
            continue  # skip the rest and ask again

        computer = random.choice(["rock", "paper", "scissors"])

        print("✊ rock")
        print("✋ paper")
        print("✌️ scissors")
        print("💥 shoot!")
        print(f"🧠 Computer chooses: {computer} {emoji[computer]}")
        print(f"🙋 You chose: {you} {emoji[you]}")

        if you == computer:
            print("😐 It's a tie!")
        elif (you == "rock" and computer == "scissors") or \
             (you == "paper" and computer == "rock") or \
             (you == "scissors" and computer == "paper"):
            print("😎 You won!")
        else:
            print("⚰️ Wasted!")

        again = input(("💀 Still alive? Dare to try again? (yes/no): ").lower())
        if again != "yes":
            print("👋 Thanks for playing!")
            break

game()
