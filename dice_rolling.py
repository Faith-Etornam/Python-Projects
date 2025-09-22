import random

while True:

    result = input('Roll the dice? (y/n): ').lower()

    if result == 'y':
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f"({num1}, {num2})")

    elif result == 'n':
        print('Thanks for playing!')
        break
    
    else:
        print('Invalid choice!')