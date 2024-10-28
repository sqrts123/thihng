import random

random_number = random.randint(1, 10)

while True:
    guess = int(input("guess a number between 1 and 10:  "))
    if guess > random_number:
        print("Too High! Try again!")
    elif guess < random_number:
        print("Too Low! Try Again")
    else:
        print("Congratulations!")
    break
