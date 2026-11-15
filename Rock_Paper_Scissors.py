import random

# Game choices
choices = ["rock", "paper", "scissors"]

# Computer selects a random choice
computer = random.choice(choices)

# User input
print("\n===== ROCK PAPER SCISSORS =====")
user = input("Choose Rock, Paper or Scissors: ").lower().strip()

# Display choices
print("\nYou chose:", user)
print("Computer chose:", computer)

# Game logic
if user not in choices:
    print("\nInvalid Choice! Please try again.")

elif user == computer:
    print("\nResult: It's a Draw! 🤝")

elif (
    (user == "rock" and computer == "scissors")
    or
    (user == "paper" and computer == "rock")
    or
    (user == "scissors" and computer == "paper")
):
    print("\nResult: Congratulations! You Win! 🎉")

else:
    print("\nResult: Computer Wins! 🤖")

print("\n===== GAME OVER =====")