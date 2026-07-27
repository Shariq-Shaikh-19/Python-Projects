import random

computer = random.choice(["Rock", "Paper", "Scissors"])

user = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

if user not in ["Rock", "Paper", "Scissors"]:
    print("Invalid choice!")
    exit()

print(f"\nYou entered: {user}")
print(f"Computer entered: {computer}\n")

if user == computer:
    print("It's a draw!")

elif (
    (user == "Rock" and computer == "Scissors") or
    (user == "Paper" and computer == "Rock") or
    (user == "Scissors" and computer == "Paper")
):
    print("You Won!")

else:
    print("You Lost!")