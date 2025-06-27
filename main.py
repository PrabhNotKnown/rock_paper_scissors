import random

# Map user input (both full word & shortcuts) to actual choice
input_map = {
    "rock": "rock", "r": "rock",
    "paper": "paper", "p": "paper",
    "scissors": "scissors", "s": "scissors"
}

# Emoji for each choice
emoji = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

def game():
    points = 0

    try:
        with open("Highscore.txt", "r") as f:
            high_score = int(f.read())
    except (FileNotFoundError, ValueError):
        high_score = 0

    print(f"🏆 Current High Score: {high_score}")

    while True:
        you = input("Choose rock ✊, paper ✋ or scissors ✌️ (or r/p/s): ").lower()

        if you in input_map:
            you = input_map[you]
        else:
            print("❌ Invalid option!")
            continue

        computer = random.choice(["rock", "paper", "scissors"])

        print("💥 Shoot!")
        print(f"🧠 Computer: {computer} {emoji[computer]}")
        print(f"🙋 You: {you} {emoji[you]}")

        if you == computer:
            print("😐 It's a tie!")
        elif (you == "rock" and computer == "scissors") or \
             (you == "paper" and computer == "rock") or \
             (you == "scissors" and computer == "paper"):
            print("😎 You won!")
            points += 1
        else:
            print("⚰️ Wasted!")
            points -= 1

        print(f"🎯 Your Score: {points}")
        print(f"🏆 High Score: {high_score}")

        if points > high_score:
            print("🎉 Wohoo! You broke the high score!")
            print(f"Previous: {high_score} → New: {points}")
            high_score = points
            with open("Highscore.txt", "w") as f:
                f.write(str(points))

        again = input("💀 Still alive? Dare to try again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break

game()
