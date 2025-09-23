import random

items = ('r', 'p', 's')

emojis = {
    'r': '🪨',
    'p': '📃',
    's': '✂️'
}

def user_selection():
    while True:
        user_select = input('Rock, paper, or scissors? (r/p/s): ').lower()

        if user_select not in items:
            print('Invalid choice!')
            continue
        return user_select    
    
def displaying_info(user_select, computer_choice):
    print(f"You chose {emojis[user_select]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determining_winner(user_select, computer_choice):
    if user_select == computer_choice:
        print('It is a tie!')

    elif (user_select == 'r' and computer_choice == 's') or \
        (user_select == 'p' and computer_choice == 'r') or \
        (user_select == 's' and computer_choice == 'p'):
        print('You win!')

    else: 
        print('You lose!')

def continue_game():
    while True:
        continue_game = input('Continue? (y/n): ').lower()
        if continue_game == 'y':
            return True
        elif continue_game == 'n':
            return False


def play_game():
    while True:
        user_select = user_selection()

        random_number = random.randint(0,2)
        computer_choice = items[random_number]

        displaying_info(user_select, computer_choice)

        determining_winner(user_select, computer_choice)
        
        if not continue_game():
            break

play_game() 

    

    

    
