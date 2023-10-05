from random import randint

real_number = randint(1, 100)
attempts = 1

while attempts <= 10:
    guessed_number = int(input("Guess a number between 1 and 100: "))
    if guessed_number == real_number:
        print("Genious! You guessed it correct.")
        print(f"You gueesed it in {attempts} number of attempts.")
        break
    elif guessed_number <= real_number:
        print("Try guessing a bigger number.")
    else:
        print("Try guessing a smaller one!")
    attempts = attempts + 1

if attempts > 10:
    print("Sorry you couldn't guess it properly. Best of luck for the next time.")
