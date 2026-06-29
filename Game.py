import random

list1 = ['Rock','Paper','Scissor']

user_score = 0
system_score = 0

while True:
    user_choice = input('Enter your move (Rock/Paper/Scissor): ').strip().capitalize()

    if user_choice not in list1:
        print('Please enter a valid choice(Rock, Paper, Scissor).\n')
        continue

    system_choice = random.choice(list1)

    print("User's choice:", user_choice, " | System's choice:", system_choice)

    if user_choice == system_choice:
        print('Match Tie')


    elif user_choice == 'Rock':
        if system_choice == 'Paper':
             print('Paper covers Rock. You Lose:(')
             system_score += 1
        else:
            print('Rock smashes scissor. You Win!')
            user_score += 1

              
    elif user_choice == 'Paper':
         if system_choice == 'Rock':
              print('Paper covers Rock. You Win!')
              user_score += 1
         else:
             print('Scissor cuts Paper. You Lose:(')
             system_score += 1
        
        
    elif user_choice == 'Scissor':
        if system_choice == 'Rock':
            print('Rock smashes Scissor. You Lose:(')
            system_score += 1
        else:
            print('Scissor cuts Paper. You Win!')
            user_score += 1
        

    print(f"Scoreboard -> You: {user_score} | System: {system_score}\n")

    play2 = input('Do you want to play again? (yes/no): ').strip().lower()
    if play2 not in ['yes','y']:
        print('Thanks for playing wiht us!')
        break




