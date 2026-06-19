import random

health = 5
system_guess = random.randint(1,20)

while health!=0:
    print(f"Your health is {health}")
    user_guess = int(input('guess a number: '))

    if user_guess < system_guess:
        print('guess bigger!')
    elif user_guess > system_guess:
        print('guess smaller')
    elif user_guess == system_guess:
        print('You won!!!')
        break
    health-=1