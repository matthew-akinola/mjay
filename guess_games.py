import random


def lorpeh_my_love(a:int, b:int):
    try:
        return a*b
    except Exception as error:
        print(error)



def guess_number():
    x = int(input("enter your guess number from 1 to 5: "))
    lifeline = 0
    while lifeline < 5:
        computer_guess = random.randint(0, 5)
        if x == computer_guess:
            print('number guessed correctly ', computer_guess )
            break
        else:
            print('opppss!! incorrect guess, try again')
            lifeline +=1
            x = int(input("enter your guess number from 1 to 5: "))
    print("game over....")

lorpeh_my_love('y','u')
# guess_number()