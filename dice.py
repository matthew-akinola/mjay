from random import randint


def dice_roll(dice_number, dice_sides):
    total_dice_rolled = 0
    dice_list = []
    for roll in range(dice_number):
        # randomly pick a side between the range of the dice sides
        number_generated = randint(0, dice_sides)
        total_dice_rolled +=number_generated
        # append the randomly pick dice-side to the list and sort in ascending other
        dice_list.append(number_generated), dice_list.sort()
        print(f"numbers generated: ", number_generated)
    print("the total is ", total_dice_rolled)
    # return the highest number using a negative array indexing
    print("the highest rolled ", dice_list[-1])


def dice_rolls():
    try:
        dice_number=int (input("enter dice number: "))
        dice_sides= int (input(" enter dice side: "))
        total_dice_rolled = 0
        dice_list = []
        for roll in range(dice_number):
            number_generated = randint(0, dice_sides)
            total_dice_rolled +=number_generated
            dice_list.append(number_generated), dice_list.sort()
            print(f"numbers generated: ", number_generated)
        print("the total is ", total_dice_rolled)
        print("the highest rolled ", dice_list[-1])
    except ValueError:
        print ("dice size and number type must be an integer")
        dice_rolls()



x = dice_rolls()
