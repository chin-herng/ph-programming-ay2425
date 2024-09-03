import random

key = random.randint(1, 100)
count = 0

while True:
    count = count + 1
    guess = int(input("Input your guess! "))
    if guess == key:
        print(f"You found the key in {count} attempts!")
        break
    elif guess > key:
        print("Guess a smaller number!")
    else:
        print("Guess a larger number!")