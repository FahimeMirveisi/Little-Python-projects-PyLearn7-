import random

dice_num = random.randint(1, 6)


if dice_num == 6:
    second_dice_roll_num = random.randint(1, 6)
    print('dice_number_in_first_roll = ', dice_num)
    print('dice_number_in_second_roll = ', second_dice_roll_num)
else:
    print('dice_number = ',dice_num)
