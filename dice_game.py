from helper import Dice

name = input("Hey there! What's your name? ")
print(f"Hey There, {name}. Welcome to the Dice Game!")

dice_one = Dice()
dice_two = Dice()

game_status = ''
while game_status != 'q':
    total = dice_one.roll_dice() + dice_two.roll_dice()

    if total == 11:
        print(f"Congrats {name}, you win!")
        print(f"Score: {total}")
    elif (total == 2) or (total == 3) or (total == 12):
        print(f"You Lose!")
        print(f"Score: {total}")
    else:
        print(f"Score: {total}")

    game_status = input("Press any key to continue. Press q to quit!")
