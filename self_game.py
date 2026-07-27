import random

n = random.randint(1, 50)

guess = 0
print("\nGuess the number between 1 to 50")

while True:
    try:
        print()
        a = int(input("Enter the number: "))
    except ValueError:
        print(f"Please enter a valid integer number.")
        continue
    
    guess += 1
    if a < n:
        print("Higher number please")
        print()
    elif a > n:
        print("Lower number please")
        print()
    else:
        print(f"You have guessed the number {n} in {guess} chances")
        break