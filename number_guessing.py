import random

correct_number = random.randint(1, 100)

while True:
    try:
        guess_number = int(input("Guess the number between 1 and 100: "))
        if guess_number > correct_number:
            print("Too high!")
        elif guess_number < correct_number:
            print("Too low!")
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')
    

