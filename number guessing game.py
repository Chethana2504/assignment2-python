
# Question 16 - Number Guessing Game


import random

number = random.randint(1, 100)
attempts = 7

print("Guess the number between 1 and 100")
print("You have 7 attempts")

for i in range(1, 8):

    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You guessed it in", i, "attempts")
        break

    elif guess > number:
        print("Too High")

    else:
        print("Too Low")

    print("Attempts left:", 7 - i)

else:
    print("You failed! The number was:", number)