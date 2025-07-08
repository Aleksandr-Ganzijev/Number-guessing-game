import random
def play_game():
    print("Welcome to the number guessing game!\n"
          "I'm thinking of a number between 1 and 100.\n"
          "You have x chances to guess the correct number.\n\n"
          "Please select the difficulty level.\n"
          "1. Easy (10 chances)\n"
          "2. Medium (5 chances)\n"
          "3. Hard (3 chances)")
    while True:
        difficulty=input("Enter your choice:" )
        if difficulty=='1':
            chances=10
            print('Great! You have selected the Easy difficulty level.')
            break
        elif difficulty=='2':
            chances=5
            print('Fantastic! You have selected the Medium difficulty level')
            break
        elif difficulty=='3':
            chances=3
            print('Hard difficulty it is, good luck!')
            break
        else:
            print('wrong input, please select the difficulty again')
    print('Let\'s start the game!')
    #game logic
    secret=random.randint(1,100)
    remaining_chances=chances
    guessed_correctly=False
    while remaining_chances>0 and not guessed_correctly:
        print('Remaining chances:', remaining_chances)
        user_input=int(input('Enter your guess: '))
        if user_input>secret:
            print('Your number is lower')
        elif user_input<secret:
            print('Your number is higher')
        else:
            print(f'You got it! The number was {secret}! You guessed it in {chances-remaining_chances+1} attempts')
            guessed_correctly=True
            break
        remaining_chances-=1
    if guessed_correctly==False:
        print(f'Oh no, the secret number was {secret}, better luck next time!')
    
while True:
    play_game()
    play_again=input('\nPlay again?(y/n): ')
    if play_again!='y':
        print('\nThanks for playing! Goodbye!')
        break
    
    
        
